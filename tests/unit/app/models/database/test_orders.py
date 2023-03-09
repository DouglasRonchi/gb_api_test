import unittest
from datetime import datetime

import pytest
from mongoengine import connect, disconnect

from app.models.database.order import Order


class TestOrderModel(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(
            db="mongomock", host="mongomock://localhost", uuidRepresentation="standard"
        )
        order = Order()
        order.code = "12345"
        order.value = 250
        order.cpf = "12345678988"
        order.status = "In validation"
        order.date = datetime(2023, 3, 1)
        order.created_at = datetime(2023, 3, 1)
        order.save_safe()

    def tearDown(self) -> None:
        disconnect()

    def test_when_save_a_new_order_with_cpf_of_more_then_eleven_digits(self):
        order = Order()
        order.code = "12345"
        order.value = 250
        order.cpf = "1535094605612345"
        order.status = "In validation"
        order.date = datetime(2023, 3, 1)
        order.created_at = datetime(2023, 3, 1)

        with pytest.raises(Exception) as err:
            order.save_safe()

        self.assertEqual("ValidationError", err.typename)


if __name__ == "__main__":
    unittest.main()
