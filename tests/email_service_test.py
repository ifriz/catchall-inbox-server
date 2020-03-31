from email.message import Message

import pytest
from email_service import email_service


@pytest.fixture
def connection():
    """ returns an instance of connection """
    service = email_service.EmailService()
    connection = service.open_connection(verbose=True)
    return connection

def test_pass():
    assert True == True

def test_open_connection():
    assert connection is not None


def test_email_find():
    service = email_service.EmailService()
    c = service.open_connection(verbose=True)

    c.noop()
    c.logout()

def test_get_emails():
    service = email_service.EmailService()
    emails = service.get_emails('iantest.20190603.1607@devshop.works')

    assert len(emails) > 0


# def test_email_is_message():
#     service = email_service.EmailService()
#     emails = service.get_emails('iantest.20190603.1607@devshop.works')
#
#     assert isinstance(emails[0]['message'], Message)

def test_get_email_by_id():
    service = email_service.EmailService()
    email_message = service.get_email_by_id(b'3215')

    assert email_message.get('subject') is not None




