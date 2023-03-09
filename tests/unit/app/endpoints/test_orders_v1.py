import http
import json
import os
import unittest
from http import HTTPStatus
from unittest.mock import patch, Mock

import pytest
from fastapi.testclient import TestClient
from mongoengine import connect, disconnect

from app.models.database.seller import Seller
from app.utils.authentication import generate_token
from tests.db_test_data.orders import order_data
from tests.db_test_data.sellers import load_sellers_db_data

os.environ.setdefault("MONGODB_URI", "test")


class TestOrdersEndpoints(unittest.TestCase):
    def setUp(self) -> None:
        from app.main import app

        self.client = TestClient(app)
        disconnect()
        connect(
            db="mongomock", host="mongomock://localhost", uuidRepresentation="standard"
        )
        seller = Seller()
        seller.name = "Fulano de Tal"
        seller.cpf = "12345678900"
        seller.email = "testr@test.com"
        seller.password = "123456"
        seller.save_safe()

        self.authentication_token = generate_token("test@test.com")

    def tearDown(self) -> None:
        disconnect()

    def test_when_create_new_order_should_return_200(self):
        body = json.dumps({
          "code": 1599,
          "value": 758,
          "cpf": "12345678900",
          "date": "2023-03-09T13:44:49.022139",
          "created_at": "2023-03-09T13:44:49.022139",
          "updated_at": "2023-03-09T13:44:49.022139"
        })
        response = self.client.post(
            "gb/v1/order",
            content=body,
            headers={"Authorization": self.authentication_token},
        )

        self.assertEqual(http.HTTPStatus.CREATED, response.status_code)

    def test_when_get_orders_with_and_without_cpf_approved_settings(self):
        load_sellers_db_data()

        self.client.post(
            "gb/v1/order",
            content=json.dumps(order_data[0]),
            headers={"Authorization": self.authentication_token},
        )

        self.client.post(
            "gb/v1/order",
            content=json.dumps(order_data[1]),
            headers={"Authorization": self.authentication_token},
        )

        self.client.post(
            "gb/v1/order",
            content=json.dumps(order_data[2]),
            headers={"Authorization": self.authentication_token},
        )

        response = self.client.get(
            "gb/v1/orders",
            headers={"Authorization": self.authentication_token},
        )

        content = json.loads(response.content)
        self.assertEqual(http.HTTPStatus.OK, response.status_code)
        self.assertEqual(content[0]["Status"], "In validation")
        self.assertEqual(content[1]["Status"], "In validation")
        self.assertEqual(content[2]["Status"], "Approved")

    @patch("app.services.order.requests")
    def test_when_get_cashback_informations_from_external_api(self, requests_mock):
        response_mock = Mock()
        requests_mock.get.return_value = response_mock
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "statusCode": 200,
            "body": {
                "credit": 2696
            }
        }

        response = self.client.get(
            "gb/v1/order/12345678900",
            headers={"Authorization": self.authentication_token},
        )

        self.assertEqual(http.HTTPStatus.OK, response.status_code)
        self.assertEqual(b'{"statusCode":200,"body":{"credit":2696}}', response.content)


if __name__ == "__main__":
    unittest.main()
