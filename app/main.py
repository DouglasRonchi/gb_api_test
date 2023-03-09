"""
This is a main API module
"""
from fastapi import FastAPI
from loguru import logger

from app.api.custom_open_api import custom_openapi
from app.db.mongo.mongo_repository import MongoDB
from app.endpoints.orders_v1 import orders_endpoint_v1_router
from app.endpoints.healthcheck import health_check_router
from app.endpoints.sellers_v1 import sellers_endpoint_v1_router
from app.middlewares.register_middlewares import RegisterMiddlewares

logger.info(f"Starting API")
app = FastAPI(
    title="API Rest GB"
)


@app.on_event("startup")
async def create_db_client():
    try:
        MongoDB().connect()
    except Exception as err:
        logger.error(f"{err}")


RegisterMiddlewares(app)

app.include_router(health_check_router, tags=["HealthCheck"])
app.include_router(orders_endpoint_v1_router, prefix="/gb/v1", tags=["Orders"])
app.include_router(sellers_endpoint_v1_router, prefix="/gb/v1", tags=["Sellers"])

app.openapi = custom_openapi
