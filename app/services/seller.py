"""
A Seller service module
"""
from loguru import logger

from app.repository.seller import SellerRepository
from app.schemas.seller import SellerSchema, SellerLoginSchema


class SellerService:
    @classmethod
    def create_new_seller(cls, seller: SellerSchema) -> SellerSchema:
        logger.info("The method create_new_seller was called")
        return SellerRepository().create(seller)

    @classmethod
    def validate_seller_login(cls, seller: SellerLoginSchema):
        logger.info("The method validate_seller_login was called")
        seller_object = SellerRepository().get_by_email(seller)
        if seller_object and seller_object.password == seller.password:
            return True
        return False
