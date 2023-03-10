"""
Schema for Order
"""
from datetime import datetime
from typing import Optional

import pendulum
from pendulum.parsing import ParserError
from pydantic import Field, validator, BaseModel, root_validator

from app.schemas.descriptions.orders import OrderDescriptions
from app.settings.settings import Settings


class OrderSchema(BaseModel):
    """
    Common fields of Order
    """

    code: int = Field(
        example=1589, description=OrderDescriptions.code_description
    )
    value: float = Field(
        example=22.5, description=OrderDescriptions.value_description
    )
    cpf: str = Field(
        max_length=11,
        example="12345645600",
        description=OrderDescriptions.cpf_description
    )
    date: str = Field(
        example=datetime.now(),
        default=datetime.now(),
        description=OrderDescriptions.date_description,
    )
    status: Optional[str] = Field(example="In validation", description=OrderDescriptions.status_description)
    created_at: str = Field(
        example=datetime.now(),
        default=datetime.now(),
        description=OrderDescriptions.created_at_description,
    )
    updated_at: Optional[str] = Field(
        example=datetime.now(), description=OrderDescriptions.updated_at_description
    )

    @validator("cpf")
    def cpf_must_contain_eleven_characters(cls, cpf):
        if len(cpf) != 11:
            raise ValueError("Cpf must contain exactly eleven characters")
        return cpf

    @root_validator
    def validate_all(cls, values):
        if values["cpf"] in Settings().APPROVED_CPFS:
            values["status"] = "Approved"
        else:
            values["status"] = "In validation"
        return values

    @validator("created_at")
    def parse_date(cls, created_at):
        try:
            parsed_date = pendulum.parse(created_at)
        except ParserError:
            raise ValueError("Unable to parse date. Invalid date format")
        if parsed_date.age > 100:
            raise ValueError("Invalid date format")
        return created_at
