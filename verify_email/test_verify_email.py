from verify_email.verify_email import *
import pytest

@pytest.fixture()
def setup_apple():
    return 'Granny Smith'

def test_assert_true(setup_apple):
    assert setup_apple == 'Granny Smith'

def test_regular_email_validates():
    assert is_valid_email_address('test@example.org')
    assert is_valid_email_address('user123@subdomain.example.org')
    assert is_valid_email_address('john.doe@email.example.org')


def test_valid_email_has_one_at_sign():
    assert not is_valid_email_address('john.doe')

def test_valid_email_has_only_allowed_chars():
    assert not is_valid_email_address('john,doe@example.org')
    assert not is_valid_email_address('not valid@example.org')

def test_valid_email_can_have_plus_sign():
    assert is_valid_email_address('john.doe+abc@gmail.com')

def test_valid_email_must_have_a_tld():
    assert not is_valid_email_address('john.doe@example')