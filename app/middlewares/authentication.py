import http

import jwt
from fastapi import FastAPI, Request
from loguru import logger
from starlette.responses import JSONResponse

from app.exceptions.exceptions import ForbiddenException
from app.utils.authentication import decode_token


class AuthenticationMiddleware:
    def __init__(self, app: FastAPI):
        app.middleware("http")(self)

    async def __call__(self, request: Request, call_next):
        logger.info("Authentication middleware called")
        if request.url.path not in [
            "/docs",
            "/openapi.json",
            "/",
            "/health",
            "/healthcheck",
        ]:
            token = request.headers.get("authorization")
            if not token:
                return JSONResponse(
                    status_code=http.HTTPStatus.UNAUTHORIZED,
                    content={"message": "Unauthorized to access"},
                )
            try:
                decode_token(token)
            except jwt.DecodeError:
                return JSONResponse(
                    status_code=http.HTTPStatus.UNAUTHORIZED,
                    content={"message": "Unauthorized to access"},
                )
            except ForbiddenException:
                return JSONResponse(
                    status_code=http.HTTPStatus.FORBIDDEN,
                    content={"message": "Unauthorized to access"},
                )
            except Exception as err:
                return JSONResponse(
                    status_code=http.HTTPStatus.UNAUTHORIZED,
                    content={"message": "Unauthorized to access"},
                )
        response = await call_next(request)
        return response
