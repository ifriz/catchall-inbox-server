import json
import logging
import re
from pycnic.core import Handler
from pycnic.errors import HTTP_400
from email_service import email_service


class EmailHandler(Handler):
    logger = logging.getLogger("catchall_inbox_server")

    def post(self):
        """ get an emails for the specified email address """

        if not self.request.data.get('email'):
            raise HTTP_400("provide an email address")

        email_address = self.request.data.get('email')

        # check to see if the email address looks valid
        email_regex = r"^([\w\.\-_]+)?\w+@[-_\w]+(\.\w+)+$"
        if not re.search(email_regex, email_address):
            raise HTTP_400("invalid email address")

        self.logger.info(f"fetching emails for {email_address}")
        service = email_service.EmailService()
        emails_response = service.get_emails(email_address)

        response = {
            "success": emails_response["success"],
            "data": []
        }

        for email in emails_response["emails"]:
            message_data = {
                "id": email["id"],
                "email": email.get("message")["from"],
                "subject": email.get("message")["subject"]
            }
            response["data"].append(message_data)

        return response

    def get(self):
        if not self.request.args.get('mid'):
            raise HTTP_400("no message id listed")

        message_id = self.request.args.get('mid')

        self.logger.info(f'fetching message {message_id}')

        service = email_service.EmailService()
        email_message = service.get_email_by_id(message_id)

        if email_message is None:
            return (
                {
                    "response": "no message found"
                }
            )

        return (
            {
                # "headers": email_message['headers'],
                # "to": email_message['to'],
                "from": email_message['from'].decode('utf-8'),
                "body": json.dumps(email_message['body'].decode('utf-8'))
            }
        )
