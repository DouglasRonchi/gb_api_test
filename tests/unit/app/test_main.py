import unittest
from unittest.mock import patch


class TestMain(unittest.TestCase):
    @patch("app.main.MongoDB")
    def test_custom_open_api(self, mongo_mock):
        from app.main import custom_openapi

        custom_openapi()

    @patch("app.main.FastAPI")
    @patch("app.main.MongoDB")
    def test_custom_open_api_with_schema(self, mongo_mock, fastapi_mock):
        from app.main import custom_openapi

        fastapi_mock.openapi_schema = True
        custom_openapi()


if __name__ == "__main__":
    unittest.main()
