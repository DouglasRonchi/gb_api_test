import os
import unittest

from mongoengine import connect, disconnect


class TestOrdersRepository(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(
            db="mongomock", host="mongomock://localhost", uuidRepresentation="standard"
        )

        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
        os.environ.setdefault("MONGODB_URI", "test")

    def tearDown(self) -> None:
        disconnect()


if __name__ == "__main__":
    unittest.main()
