"""
Register Middlewares module
"""
from fastapi import FastAPI

from app.middlewares.authentication import AuthenticationMiddleware


class RegisterMiddlewares:
    def __init__(self, app: FastAPI):
        AuthenticationMiddleware(app)
