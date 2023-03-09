"""
Sellers Descriptions Class
"""


class SellerDescriptions:
    id_description = "Seller identification code."
    name_description = "The Seller Name. String format."
    cpf_description = (
        "Seller CPF number. Enter only the numbers, without dots and dash (12345678900, for example). "
        "Required field."
    )
    email_description = "Seller email. Enter only string."
    password_description = "Seller password. Accept all Characters."
    created_at_description = (
        "Seller's register created at. Use the YYYY-MM-DD format (1998-07-23, for example). The "
        "date must be less than today's date and greater than 1900-01-01. Required field. "
    )
    updated_at_description = (
        "Seller's register updated at. Use the YYYY-MM-DD format (1998-07-23, for example). The "
        "date must be less than today's date and greater than 1900-01-01. Required field. "
    )
