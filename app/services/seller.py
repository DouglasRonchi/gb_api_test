"""
A Seller service module
"""
from app.repository.seller import SellerRepository
from app.schemas.seller import SellerSchema, SellerLoginSchema


class SellerService:
    @classmethod
    def create_new_seller(cls, seller: SellerSchema) -> SellerSchema:
        return SellerRepository().create(seller)

    @classmethod
    def validate_seller_login(cls, seller: SellerLoginSchema):
        seller_object = SellerRepository().get_by_email(seller)
        if seller_object and seller_object.password == seller.password:
            return True
        return False
