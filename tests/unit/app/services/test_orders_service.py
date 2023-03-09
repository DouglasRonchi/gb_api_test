import os
import unittest

from mongoengine import connect, disconnect

from app.models.database.seller import Seller
from app.schemas.order import OrderSchema
from app.services.order import OrderService


class TestOrdersService(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(
            db="mongomock", host="mongomock://localhost", uuidRepresentation="standard"
        )

        seller = Seller()
        seller.name = "Fulano"
        seller.cpf = "15350946056"
        seller.email = "testing@testing.com"
        seller.password = "654321"
        seller.save_safe()

        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
        os.environ.setdefault("MONGODB_URI", "test")

    def tearDown(self) -> None:
        disconnect()

    def test_when_create_a_new_order_must_return_object_created(self):
        data = {
            "code": "1569",
            "value": 758,
            "cpf": "15350946056",
            "date": "2023-03-02",
            "created_at": "2023-03-02",
            "updated_at": "2023-03-02",
        }

        order = OrderSchema(**data)

        response = OrderService().create_new_order(order)

        self.assertTrue(response.id)
        self.assertEqual(1569, response.code)
        self.assertEqual(758, response.value)
        self.assertEqual("15350946056", response.cpf)
        self.assertEqual("Approved", response.status)
        self.assertEqual("2023-03-02", response.date)
        self.assertEqual("2023-03-02", response.created_at)


if __name__ == "__main__":
    unittest.main()
