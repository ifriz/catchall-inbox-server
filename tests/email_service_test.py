from email_service import email_service


def test_pass():
    assert True is True


def test_get_email_load_credentials_from_file():
    service = email_service.EmailService()
    assert service.hostname is not None


def test_get_email_invalid_address():
    service = email_service.EmailService()
    response = service.get_emails('@example.com')
    assert response["success"] is False


def test_get_email_not_provided():
    service = email_service.EmailService()
    response = service.get_emails(None)
    assert response["success"] is False


def test_get_email_does_not_exist():
    service = email_service.EmailService()
    response = service.get_emails("test@example.com")
    assert response["success"] is False


# To test a successful request to get an email, uncomment this test
# Provide an email address that is known to exist in the mailbox.
# def test_get_emails_is_successful():
#     service = email_service.EmailService()
#     response = service.get_emails('test@example.com')
#     assert response["success"] is True


# To test a successful request to get an email, uncomment this test
# Provide an email address that is known to exist in the mailbox.
# def test_get_emails_has_values():
#     service = email_service.EmailService()
#     response = service.get_emails('test@example.com')
#     assert len(response["emails"]) > 0


def test_get_email_by_invalid_id():
    s = email_service.EmailService()
    m = s.get_email_by_id(b'1')
    assert m is None

# To test for a successful call to get an email by ID, uncomment this test and provide a known email message id
# def test_get_email_by_id():
#     service = email_service.EmailService()
#     email_message = service.get_email_by_id(b'0000')
#     assert email_message.get('subject') is not None
