"""
Order Descriptions Class
"""


class OrderDescriptions:
    id_description = "Order identification code."
    code_description = "The Order Code. Integer format."
    value_description = "The Order Value. Float format."
    cpf_description = (
        "Order CPF number. Enter only the numbers, without dots and dash (12345678900, for example). "
        "Required field."
    )
    date_description = (
        "Order date. Use the YYYY-MM-DD format (1998-07-23, for example). The"
        "date must be less than today's date and greater than 1900-01-01. Required field. "
    )
    status_description = (
        "Order status. String format. Possible Status: [In validation, Approved]"
    )
    created_at_description = (
        "Order's register created at. Use the YYYY-MM-DD format (1998-07-23, for example). The "
        "date must be less than today's date and greater than 1900-01-01. Required field. "
    )
    updated_at_description = (
        "Order's register updated at. Use the YYYY-MM-DD format (1998-07-23, for example). The "
        "date must be less than today's date and greater than 1900-01-01. Required field. "
    )
