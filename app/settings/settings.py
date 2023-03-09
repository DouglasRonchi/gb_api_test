"""
This is a project settings module
"""
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    MONGODB_URI: str = Field(
        "mongodb://root:example@localhost:27017/gb_api?authSource=admin",
        env="MONGODB_URI",
    )
    SECRET_KEY_AUTH_SAML: str = Field("testsecretkey", env="SECRET_KEY_AUTH_SAML")
    APPROVED_CPFS: list = Field(["15350946056"], env="APPROVED_CPFS")
    URL_GB: str = Field("https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com", env="URL_GB")
    URL_GB_TOKEN: str = Field("ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm", env="URL_GB_TOKEN")
