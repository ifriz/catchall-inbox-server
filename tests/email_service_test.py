from email.message import Message

import pytest
from email_service import email_service


def test_pass():
    assert True == True


def test_get_email_load_credentials_from_file():
    service = email_service.EmailService()
    assert service.hostname is not None


# To test a successful request to get an email, uncomment this test
# Provide an email address that is known to exist in the mailbox.
# def test_get_emails():
#     service = email_service.EmailService()
#     emails = service.get_emails('existingemail@example.com')
#
#     assert len(emails) > 0


def test_get_email_not_provided():
    service = email_service.EmailService()
    emails = service.get_emails(None)

    assert emails is None


def test_get_email_invalid_email():
    service = email_service.EmailService()
    emails = service.get_emails("abcd")

    assert emails is None


def test_get_email_by_invalid_id():
    s = email_service.EmailService()
    m = s.get_email_by_id(b'1')

    assert m is None

# To test for a successful call to get an email by ID, uncomment this test and provide a known email message id
# def test_get_email_by_id():
#     service = email_service.EmailService()
#     email_message = service.get_email_by_id(b'3215')
#
#     assert email_message.get('subject') is not None
