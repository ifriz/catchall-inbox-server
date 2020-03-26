from pycnic.core import Handler
from pycnic.errors import HTTP_400

from email_service import email_service


class EmailHandler(Handler):

    def post(self):
        """ get an emails for the specified email address """

        if not self.request.data.get('email'):
            raise HTTP_400("provide an email address")

        email_address = self.request.data.get('email')

        emails = []
        # emails

        service = email_service.EmailService()

        emails = service.find_emails(email_address)

        data = []

        for email in emails:
            message_data = {
                "id": email["id"],
                "email": email.get("message")["from"],
                "subject": email.get("message")["subject"]
            }
            data.append(message_data)

        return data
