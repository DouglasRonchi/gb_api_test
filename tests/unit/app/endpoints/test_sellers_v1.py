import json
import os
import unittest
from http import HTTPStatus

from fastapi.testclient import TestClient
from mongoengine import connect, disconnect

from app.utils.authentication import generate_token

os.environ.setdefault("MONGODB_URI", "test")


class TestSellerEndpoints(unittest.TestCase):
    def setUp(self) -> None:
        from app.main import app

        self.client = TestClient(app)
        disconnect()
        connect(
            db="mongomock", host="mongomock://localhost", uuidRepresentation="standard"
        )
        self.authentication_token = generate_token("test@test.com")

    def tearDown(self) -> None:
        disconnect()

    def test_when_create_new_seller_should_return_200(self):
        body = json.dumps({
            "name": "Fulano",
            "cpf": "15350946056",
            "email": "test1@test.com",
            "password": "1234@abcd",
            "created_at": "2023-03-09T10:15:34.905920"
        })
        response = self.client.post(
            "gb/v1/seller",
            content=body,
            headers={"Authorization": self.authentication_token},
        )

        self.assertEqual(HTTPStatus.OK, response.status_code)


if __name__ == "__main__":
    unittest.main()
