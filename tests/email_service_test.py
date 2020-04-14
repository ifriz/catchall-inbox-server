from email.message import Message

import pytest
from email_service import email_service


def test_pass():
    assert True == True


def test_get_emails():
    service = email_service.EmailService()
    emails = service.get_emails('iantest.20190603.1607@devshop.works')

    assert len(emails) > 0


def test_get_email_by_invalid_id():
    s = email_service.EmailService()
    m = s.get_email_by_id(b'1')

    assert m is None


def test_get_email_by_id():
    service = email_service.EmailService()
    email_message = service.get_email_by_id(b'3215')

    assert email_message.get('subject') is not None
