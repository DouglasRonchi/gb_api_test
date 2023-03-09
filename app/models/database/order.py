"""
Mongo order model
"""
from datetime import datetime

from mongoengine import DateTimeField, Document, IntField, StringField, SequenceField

from app.db.mongo.mongo_safe_document import SafeDocument


class Order(Document, SafeDocument):
    id = SequenceField(primary_key=True, required=True)
    code = IntField(required=True)
    value = IntField(required=False)
    cpf = StringField(required=True, max_length=11)
    status = StringField(required=True, default="In validation")
    date = DateTimeField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    updated_at = DateTimeField(required=False)

    meta = {"collection": "orders", "indexes": ["code", "cpf"]}
