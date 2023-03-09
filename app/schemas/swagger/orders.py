"""
Swagger documentation for order schema module
"""
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str


class OrderResponseOK(BaseModel):
    id: str
    name: str
    city: str
    created_at: datetime
    updated_at: datetime


class BadRequestPattern(BaseModel):
    type: str = "InvalidDate"
    error: str = "Data Inválida"
    detail: str = "Data de criação inválida"
    instance: str = "/orders/1"
    trace_id: str = "237462837462102342"


get_seller_cashback = {
    200: {
        "model": OrderResponseOK,
        "description": "When get all permissions successfully",
    },
    204: {"description": "Cannot find any order on database"},
    404: {"model": Message, "description": "The permissions cannot be retrieved"},
    400: {
        "model": BadRequestPattern,
        "description": "Sending invalid data (data types, values)",
    },
}

create_new_order_responses = {
    201: {"model": None, "description": "When order was created successfully"},
    404: {"model": Message, "description": "Not Found"},
    400: {
        "model": BadRequestPattern,
        "description": "Sending invalid data (data types, values)",
    },
}
