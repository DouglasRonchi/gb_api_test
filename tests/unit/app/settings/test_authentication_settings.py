import os
import unittest

from app.settings.settings import Settings

os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
os.environ.setdefault("MONGODB_URI", "testing")


class TestAuthenticationSettings(unittest.TestCase):
    def test_authentication_settings(self):
        authentication = Settings()
        self.assertEqual("testsecretkey", authentication.SECRET_KEY_AUTH_SAML)


if __name__ == "__main__":
    unittest.main()
