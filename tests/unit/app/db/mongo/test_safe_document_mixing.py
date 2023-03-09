"""
This is a test safe document mixing module
"""
import unittest
from unittest.mock import patch

from mongoengine import Document, QuerySet, StringField, connect, disconnect

from app.db.mongo.mongo_safe_document import SafeDocument
from app.exceptions.exceptions import MongoObjectsException, MongoSaveException


class TestSafeDocumentMixin(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(
            db="mongomock", host="mongomock://localhost", uuidRepresentation="standard"
        )

    def tearDown(self) -> None:
        disconnect()

    def test_initialize_safe_document_mixing(self):
        SafeDocument()

    def test_save_safe_with_success(self):
        class TestModel(Document, SafeDocument):
            test_field = StringField()
            meta = {"collection": "test_collection"}

        object_created = TestModel(test_field="test_value").save_safe()
        self.assertIsInstance(object_created, TestModel)
        self.assertEqual(object_created.test_field, "test_value")
        self.assertEqual(len(TestModel.objects.all()), 1)

    @patch("app.db.mongo.mongo_safe_document.time")
    def test_save_safe_with_error(self, time_mock):
        class TestModel(Document, SafeDocument):
            test_field = StringField()
            meta = {"collection": "test_collection", "allow_inheritance": True}

        class OverrideTestModel(TestModel):
            def save(*args, **kwargs):
                raise MongoSaveException

        object_created = OverrideTestModel(test_field="test_value").save_safe()

        self.assertEqual(object_created, None)
        self.assertEqual(time_mock.sleep.call_count, 5)

    def test_objects_safe_with_success(self):
        class TestModel(Document, SafeDocument):
            test_field = StringField()
            meta = {"collection": "test_collection"}

        objects_results = TestModel.objects_safe()
        self.assertIsInstance(objects_results, QuerySet)
        self.assertEqual(list(objects_results), [])

    @patch("app.db.mongo.mongo_safe_document.time")
    def test_objects_safe_with_error(self, time_mock):
        class TestModel(Document, SafeDocument):
            test_field = StringField()
            meta = {"collection": "test_collection", "allow_inheritance": True}

        class OverrideTestModel(TestModel):
            def objects(*args, **kwargs):
                raise MongoObjectsException

        test_model_instance = OverrideTestModel()
        objects_results = test_model_instance.objects_safe()

        self.assertEqual(objects_results, None)
        self.assertEqual(time_mock.sleep.call_count, 5)
