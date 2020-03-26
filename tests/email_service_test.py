import pytest
from email_service import email_service
import imaplib

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


