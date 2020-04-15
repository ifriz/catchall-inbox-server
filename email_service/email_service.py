import os
import email
import logging
import re
import yaml
from imapclient import IMAPClient


class EmailService():
    logger = None
    hostname, username, password = [""] * 3

    def __init__(self):

        self.logger = logging.getLogger("catchall_inbox_server")

        if "CATCHALL_HOSTNAME" in os.environ:
            self.hostname = os.environ["CATCHALL_HOSTNAME"]
            self.username = os.environ["CATCHALL_USERNAME"]
            self.password = os.environ["CATCHALL_PASSWORD"]

        elif os.path.exists(os.path.dirname(__file__) + '/../credentials.yml'):
            with open(os.path.dirname(__file__) + '/../credentials.yml') as f:
                credentials_data = yaml.load(f, Loader=yaml.FullLoader)
                self.hostname = credentials_data["hostname"]
                self.username = credentials_data["username"]
                self.password = credentials_data["password"]
                self.logger.info("Loaded credentials from file")

        else:
            self.logger.warning("Failure to load credential data")

    def get_emails(self, email_address=None):

        # did we get anything in the request?
        if email_address is None:
            self.logger.warning("No email address provided")
            return

        # does the provided email address at least look like an email address?
        email_regex = r"^([\w\.\-_]+)?\w+@[-_\w]+(\.\w+)+$"
        if not re.search(email_regex, email_address):
            return

        emails = []

        # lets go look for messages for a matching email address
        try:
            with IMAPClient(host=self.hostname) as client:
                client.login(self.username, self.password)
                client.select_folder("INBOX")

                messages = client.search(['NOT', 'DELETED', 'TO', email_address])

                response = client.fetch(messages, ['RFC822'])

                if len(response) == 0:
                    self.logger.debug(f"no message found for email: {email_address}")
                    return None

                # `response` is keyed by message id and contains parsed,
                # converted response items.
                for message_id, message_data in response.items():
                    email_message = email.message_from_bytes(message_data[b'RFC822'])
                    emails.append({"id": message_id, "message": email_message})
                    print(message_id, email_message.get('From'), email_message.get('Subject'))

        except Exception as err:
            print("Error occurred attempting to fetch email")
            print(f"Error: {err}")

        finally:
            return emails

    def get_email_by_id(self, message_id):

        result = {}

        try:
            with IMAPClient(host=self.hostname) as client:
                client.login(self.username, self.password)
                client.select_folder("INBOX")

                response = client.fetch(message_id, ['RFC822'])
                if len(response) == 0:
                    self.logger.debug(f"no message found with id {message_id}")
                    return None

                # `response` is keyed by message id and contains parsed,
                # converted response items.
                for message_id, message_data in response.items():
                    email_message = email.message_from_bytes(message_data[b'RFC822'])
                    self.logger.info("Collecting message data for message id %d:", message_id)

                    result["from"] = email_message.get("From")
                    result["subject"] = email_message.get("Subject")

                    for parts in email_message.walk():
                        result["body"] = parts.get_payload(decode=True)

            return result

        except Exception as err:
            self.logger.error("Error occurred attempting to fetch email: %s", err)
