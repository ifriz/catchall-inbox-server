import imaplib
import configparser
import os
import email


class EmailService():

    def open_connection(self, verbose=False):
        # open an imap connections
        hostname = 'devshop.works'
        username = 'noreply@devshop.works'
        password = 'noreply@2kmlgo4U'

        if verbose:
            print(f"Connecting to {hostname}")

        # connect to host
        connection = imaplib.IMAP4_SSL(hostname)

        # login to catch-all mailbox.
        if verbose:
            print(f"Logging in to account {username}")

        connection.login(username, password)

        return connection

    def find_emails(self, email_address=None):
        c = self.open_connection(verbose=True)
        try:
            c.select(mailbox='INBOX', readonly=1)

            search_criteria = "ALL"

            if email_address is not None:
                search_criteria = f'(TO "{email_address}")'

            (retcode, msgnums) = c.search(None, search_criteria)

            emails = []

            if retcode == 'OK':
                print(f'messages found for {search_criteria}')

                msg_ids = msgnums[0].split()

                print('fetching messages')
                for msgid in msg_ids:
                    typ, message = c.fetch(msgid, '(RFC822)')
                    msg = email.message_from_bytes(message[0][1])

                    emails.append({"id": msgid, "message": msg})

                    # print(f'{msg["to"]}\n{msg["from"]}\n -- {msg["subject"]}\n')

                print('finished fetching messages')

            return emails

        except Exception as err:
            print("Error occured attempting to fetch email")
            print(f"Error: {err}")

        finally:
            c.shutdown()
