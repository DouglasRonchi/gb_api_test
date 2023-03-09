"""
Authentication module.
It helps to generate a unique token and decode it based on the secret key
"""
from datetime import datetime, timedelta
from uuid import uuid4

import jwt
from loguru import logger

from app.exceptions.exceptions import ForbiddenException, UnauthorizedException
from app.settings.settings import Settings


def decode_token(token):
    secret_key = Settings().SECRET_KEY_AUTH_SAML
    try:
        if "Bearer" in token:
            token = token.split()[-1]
        data = jwt.decode(
            token,
            secret_key,
            options={"verify_signature": True},
            algorithms=["HS256"],
        )
        return data

    except jwt.DecodeError:
        logger.warning(f"Token invalid {token}")
        raise UnauthorizedException

    except ForbiddenException:
        logger.warning("Token with access denied")
        raise ForbiddenException

    except Exception as err:
        logger.warning(f"Something happened on decode token - {err.args}")
        raise UnauthorizedException


def generate_token(email: str = ""):
    """
    :param email: Email that will be used to generate a token
    :return:
    """
    try:
        date_now = datetime.utcnow()
        exp_date = date_now + timedelta(hours=4)
        token_settings = {
            "sub": str(uuid4()),
            "email": email,
            "iat": date_now,
            "exp": exp_date,
        }
        access_token = jwt.encode(token_settings, Settings().SECRET_KEY_AUTH_SAML)
        return f"Bearer {access_token}"

    except Exception as error:
        logger.error(f"Something happened on generator token {error.args}")
        return f"Something happened on generator token {error.args}"
