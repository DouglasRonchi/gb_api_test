import os
import unittest
from unittest.mock import patch

import pytest

from app.utils.authentication import decode_token, generate_token


class TestAuthRequired(unittest.TestCase):
    @patch("app.utils.authentication.Settings")
    def test_decode_token_without_bearer(self, settings_mock):
        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testing")
        os.environ.setdefault("MONGODB_URI", "testing")
        settings_mock().SECRET_KEY_AUTH_SAML = "testing"
        token = generate_token("test@test.com")
        decode_token(token)

        self.assertTrue(settings_mock.called_once)

    @patch("app.utils.authentication.Settings")
    def test_decode_token_with_bearer(self, settings_mock):
        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testing")
        os.environ.setdefault("MONGODB_URI", "testing")
        settings_mock().SECRET_KEY_AUTH_SAML = "testing"
        token = generate_token("test@test.com")
        token = f"Bearer {token}"
        decode_token(token)

        self.assertTrue(settings_mock.called_once)

    @patch("app.utils.authentication.Settings")
    def test_decode_token_exception_decode_error(self, settings_mock):
        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testing")
        os.environ.setdefault("MONGODB_URI", "testing")
        settings_mock().SECRET_KEY_AUTH_SAML = "testing"
        token = f"Bearer 1234"
        with pytest.raises(Exception) as err:
            decode_token(token)

        self.assertEqual("UnauthorizedException", err.typename)
        self.assertTrue(settings_mock.called_once)

    @patch("app.utils.authentication.Settings")
    def test_decode_token_expired_signature_exception(self, settings_mock):
        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testing")
        os.environ.setdefault("MONGODB_URI", "testing")
        settings_mock().SECRET_KEY_AUTH_SAML = "testing"

        token = 1

        with pytest.raises(Exception) as err:
            decode_token(token)

        self.assertEqual("UnauthorizedException", err.typename)
        self.assertTrue(settings_mock.called_once)

    @patch("app.utils.authentication.Settings")
    @patch("app.utils.authentication.uuid4")
    def test_decode_token_without_bearer(self, uuid_mock, settings_mock):
        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testing")
        os.environ.setdefault("MONGODB_URI", "testing")
        settings_mock().SECRET_KEY_AUTH_SAML = "testing"
        uuid_mock.uuid4.side_effect = [Exception]

        generate_token("test@test.com")

        self.assertTrue(settings_mock.called_once)


if __name__ == "__main__":
    unittest.main()
