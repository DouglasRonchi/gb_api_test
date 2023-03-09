"""
This is a orders' endpoint module
"""

import http
import json

from fastapi import APIRouter, Depends
from loguru import logger
from starlette.responses import JSONResponse

from app.exceptions.exceptions import ForbiddenException, UnauthorizedException, SellerDoNotExistsException
from app.schemas.order import OrderSchema
from app.schemas.swagger.orders import (create_new_order_responses,
                                        get_seller_cashback)
from app.services.order import OrderService
from app.utils.authentication import decode_token

orders_endpoint_v1_router = APIRouter()


@orders_endpoint_v1_router.post("/order", responses=create_new_order_responses)
def create_new_order(order: OrderSchema):
    """
    Route to register a new purchase requiring at least code, value, date and CPF of the
    reseller).;
    """
    try:
        OrderService().create_new_order(order)
        return JSONResponse(status_code=http.HTTPStatus.CREATED, content={"Message": "Order Created!"})
    except UnauthorizedException:
        return JSONResponse(
            status_code=http.HTTPStatus.UNAUTHORIZED,
            content={"message": "Unauthorized to access"},
        )
    except ForbiddenException:
        return JSONResponse(
            status_code=http.HTTPStatus.FORBIDDEN, content={"message": "Access denied"}
        )
    except SellerDoNotExistsException:
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "The CPF informed do not exists."}
        )
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={"message": "Something went wrong"},
        )


@orders_endpoint_v1_router.get("/orders")
def get_all_orders():
    """
    Route to list registered purchases returning code, value, date, % cashback
    applied for this purchase, cashback value for this purchase and status;
    """
    try:
        data = OrderService().get_all_orders()
        data = json.dumps(data, default=str)
        return JSONResponse(
            status_code=http.HTTPStatus.OK, content=json.loads(data)
        )
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
        logger.error(f"Error {err}")
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={"message": "Something went wrong"},
        )


@orders_endpoint_v1_router.get("/order/{cpf}", responses=get_seller_cashback)
def get_cashback(cpf):
    """
    Route to display the cashback accumulated so far, this route will consume this
    information from an external API provided by the Boticário.
    """
    try:
        data = OrderService.get_accumulated_cashback(cpf)
        return JSONResponse(
            status_code=http.HTTPStatus.OK, content=data
        )
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
        logger.error(f"Error {err}")
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={"message": "Something went wrong"},
        )
