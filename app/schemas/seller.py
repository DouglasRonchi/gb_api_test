"""
Schema for Seller
"""
from datetime import datetime
from typing import Optional

import pendulum
from pendulum.parsing import ParserError
from pydantic import Field, validator, BaseModel

from app.schemas.descriptions.sellers import SellerDescriptions


class SellerSchema(BaseModel):
    """
    Common fields of Seller
    """

    name: str = Field(
        example="Test Name", description=SellerDescriptions.name_description
    )
    cpf: str = Field(
        example="12345645600", description=SellerDescriptions.cpf_description
    )
    email: str = Field(
        example="test@test.com", description=SellerDescriptions.email_description
    )
    password: str = Field(
        example="1234@abcd", description=SellerDescriptions.password_description
    )
    created_at: str = Field(
        example=datetime.now(),
        default=datetime.now(),
        description=SellerDescriptions.created_at_description,
    )
    updated_at: Optional[str] = Field(
        example=datetime.now(), description=SellerDescriptions.updated_at_description
    )

    @validator("cpf")
    def cpf_must_contain_eleven_max_characters(cls, cpf):
        if len(cpf) != 11:
            raise ValueError("Cpf must contain exactly eleven characters")
        return cpf

    @validator("created_at")
    def parse_date(cls, created_at):
        try:
            parsed_date = pendulum.parse(created_at)
        except ParserError:
            raise ValueError("Unable to parse date. Invalid date format")
        if parsed_date.age > 100:
            raise ValueError("Invalid date format")
        return created_at


class SellerLoginSchema(BaseModel):
    """
    Login fields of Seller
    """
    email: str = Field(
        example="test@test.com", description=SellerDescriptions.email_description
    )
    password: str = Field(
        example="1234@abcd", description=SellerDescriptions.password_description
    )
