"""
Seller repository module
"""
from app.models.database.seller import Seller
from app.schemas.seller import SellerSchema, SellerLoginSchema


class SellerRepository:
    """
    Class with manipulate Seller model
    """

    @staticmethod
    def create(seller: SellerSchema) -> SellerSchema:
        """
        This method save item in Seller

        :params:
            item: Dict

        :return:
            SellerSchema
        """
        return Seller(**seller.dict()).save_safe()

    @staticmethod
    def get_by_email(seller: SellerLoginSchema) -> SellerSchema:
        """
        This method get item in Seller

        :params:
            item: Dict

        :return:
            SellerLoginSchema
        """
        return Seller.objects(email=seller.email).first()

    @classmethod
    def get_by_cpf(cls, cpf):
        """
                This method get item in Seller

                :params:
                    cpf: String

                :return:
                    SellerLoginSchema
                """
        return Seller.objects(cpf=cpf).first()

