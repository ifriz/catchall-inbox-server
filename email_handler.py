import json
import logging
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

        emails = []
        # emails

        self.logger.info(f"fetching emails for {email_address}")
        service = email_service.EmailService()

        emails = service.get_emails(email_address)

        data = []

        for email in emails:
            message_data = {
                "id": email["id"],
                "email": email.get("message")["from"],
                "subject": email.get("message")["subject"]
            }
            data.append(message_data)

        return data

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
                "from": email_message['from'],
                "body": json.dumps(email_message['body'].decode('utf-8'))
            }
        )
