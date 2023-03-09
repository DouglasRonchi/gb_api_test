"""
This is an sellers' endpoint module
"""
import http

from fastapi import APIRouter
from loguru import logger
from starlette.responses import JSONResponse

from app.exceptions.exceptions import ForbiddenException, UnauthorizedException
from app.schemas.seller import SellerSchema, SellerLoginSchema
from app.services.seller import SellerService

sellers_endpoint_v1_router = APIRouter()


@sellers_endpoint_v1_router.post("/seller")
def create_new_seller(seller: SellerSchema):
    """
    Route to register a new reseller requiring at least full name, CPF,
    e-mail and password;
    """
    try:
        SellerService.create_new_seller(seller)
        return JSONResponse(
            status_code=http.HTTPStatus.OK, content={"Message": "Seller created!"})
    except UnauthorizedException:
        return JSONResponse(
            status_code=http.HTTPStatus.UNAUTHORIZED,
            content={"message": "Unauthorized to access"},
        )
    except ForbiddenException:
        return JSONResponse(
            status_code=http.HTTPStatus.FORBIDDEN, content={"message": "Access denied"}
        )
    except Exception as err:
        logger.error(f"{err}")
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={"message": "Something went wrong"},
        )


@sellers_endpoint_v1_router.get("/seller_login")
def seller_login(seller: SellerLoginSchema):
    """
    Route to validate a reseller's login;
    """
    try:
        validation = SellerService.validate_seller_login(seller)
        return JSONResponse(
            status_code=http.HTTPStatus.OK, content={"Success": validation})
    except UnauthorizedException:
        return JSONResponse(
            status_code=http.HTTPStatus.UNAUTHORIZED,
            content={"message": "Unauthorized to access"},
        )
    except ForbiddenException:
        return JSONResponse(
            status_code=http.HTTPStatus.FORBIDDEN, content={"message": "Access denied"}
        )
    except Exception as err:
        logger.error(f"{err}")
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={"message": "Something went wrong"},
        )
