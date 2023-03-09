"""
This is a project exceptions module
"""


class MongoSaveException(Exception):
    """Raise when there an error on try to save something on mongo"""


class MongoObjectsException(Exception):
    """Raise when there an error on try to query something on mongo"""


class UnauthorizedException(Exception):
    """Raise when got some error on decode token"""


class ForbiddenException(Exception):
    """Raise when got denied access to operation or resource, not authorized to access"""


class SellerDoNotExistsException(Exception):
    """Raise when do not find a specific seller on database"""
