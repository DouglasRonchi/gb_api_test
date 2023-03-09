import os
import unittest
from http import HTTPStatus

from fastapi.testclient import TestClient
from mongoengine import connect, disconnect

from app.db.mongo.mongo_repository import MongoDB

os.environ.setdefault("MONGODB_URI", "test")


class TestHealthCheck(unittest.TestCase):
    def setUp(self) -> None:
        from app.main import app

        self.client = TestClient(app)
        disconnect()
        MongoDB().connect("mongomock", host="mongomock://localhost")

    def tearDown(self) -> None:
        disconnect()

    def test_when_verify_integrity_should_return_200(self):
        response = self.client.get("/health")
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_when_verify_integrity_should_return_a_json(self):
        response = self.client.get("/health")
        self.assertEqual("application/json", response.headers["Content-Type"])

    def test_when_verify_integrity_should_return_content(self):
        response = self.client.get("/health")
        expected_response = {"status": "OK"}
        self.assertEqual(expected_response, response.json())


if __name__ == "__main__":
    unittest.main()
