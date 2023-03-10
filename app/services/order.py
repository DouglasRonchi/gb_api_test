"""
A Order service module
"""
from typing import List, Dict

import requests
from loguru import logger

from app.exceptions.exceptions import SellerDoNotExistsException, InvalidCPFException
from app.repository.order import OrderRepository
from app.repository.seller import SellerRepository
from app.schemas.order import OrderSchema
from app.settings.settings import Settings


class OrderService:
    @classmethod
    def create_new_order(cls, order: OrderSchema) -> OrderSchema:
        logger.info("The method create_new_order was called")
        if not SellerRepository.get_by_cpf(order.cpf):
            raise SellerDoNotExistsException
        return OrderRepository().create(order)

    @classmethod
    def get_all_orders(cls) -> List[Dict]:
        logger.info("The method get_all_orders was called")
        orders = OrderRepository.get_all()
        all_orders = []
        for order in orders:
            cashback_value, cashback_percentage = OrderService.get_cashback_infos(order.value)
            all_orders.append(cls.build_order_payload(cashback_percentage, cashback_value, order))
        return all_orders

    @classmethod
    def build_order_payload(cls, cashback_percentage, cashback_value, order):
        return {
            "Code": order.code,
            "Value": order.value,
            "Date": order.date,
            "Cashback Percentage": OrderService.convert_percentage(cashback_percentage),
            "Cashback Value": cashback_value,
            "Status": order.status,
        }

    @staticmethod
    def convert_percentage(cashback_percentage):
        return f"{int(cashback_percentage * 100)}%"

    @staticmethod
    def validate_cpf(cpf):
        if len(cpf) != 11:
            raise InvalidCPFException

    @staticmethod
    def get_cashback_infos(order_value):
        percentage = OrderService.get_cashback_percentage_from_order_bonus(order_value)
        cashback_value = order_value * percentage
        return cashback_value, percentage

    @staticmethod
    def get_cashback_percentage_from_order_bonus(order_value):
        if order_value < 1000:
            return 0.1
        elif 1000 <= order_value < 1500:
            return 0.15
        elif order_value > 1500:
            return 0.20

    @classmethod
    def get_accumulated_cashback(cls, cpf):
        logger.info("The method get_accumulated_cashback was called")
        response = cls.gb_api_request(cpf)
        if response.status_code == 200:
            return response.json()
        return {"Message": "The external API does not respond."}

    @classmethod
    def gb_api_request(cls, cpf):
        logger.info("Making a request from GB External API")
        url = f"{Settings().URL_GB}/v1/cashback?cpf={cpf}"
        headers = {"token": Settings().URL_GB_TOKEN}
        response = requests.get(url=url, headers=headers)
        return response
