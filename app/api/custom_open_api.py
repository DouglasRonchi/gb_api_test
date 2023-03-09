"""
Custom OpenApi Schema
"""
from fastapi.openapi.utils import get_openapi


def custom_openapi():
    from app.main import app

    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="GB API Test",
        version="1.0.0",
        openapi_version="3.0.2",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
