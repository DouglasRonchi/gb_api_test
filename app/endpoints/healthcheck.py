"""
The Project HealthCheck Module
"""
import http

from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.db.mongo.mongo_repository import MongoDB

health_check_router = APIRouter()


def is_database_ok():
    return MongoDB().check_connection()


@health_check_router.get("/health")
async def health_check():
    if not is_database_ok():
        return JSONResponse(
            status_code=http.HTTPStatus.SERVICE_UNAVAILABLE,
            content={"status": "Database is down"},
        )
    return JSONResponse(status_code=http.HTTPStatus.OK, content={"status": "OK"})


@health_check_router.get("/healthcheck")
async def health_check():
    return JSONResponse(status_code=http.HTTPStatus.OK, content={"status": "OK"})
