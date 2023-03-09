"""
Order repository module
"""
from app.models.database.order import Order
from app.schemas.order import OrderSchema


class OrderRepository:
    """
    Class with manipulate Order model
    """

    @staticmethod
    def create(order: OrderSchema) -> OrderSchema:
        """
        This method save item in Order

        :params:
            item: Dict

        :return:
            OrderSchema
        """
        return Order(**order.dict()).save_safe()

    @classmethod
    def get_all(cls):
        return Order.objects().all()
