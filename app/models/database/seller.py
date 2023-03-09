"""
Mongo order model
"""
from datetime import datetime

from mongoengine import DateTimeField, Document, IntField, StringField, SequenceField

from app.db.mongo.mongo_safe_document import SafeDocument


class Seller(Document, SafeDocument):
    id = SequenceField(primary_key=True, required=True)
    name = StringField(required=True)
    cpf = StringField(required=True, unique=True, max_length=11)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    updated_at = DateTimeField(required=False)

    meta = {"collection": "sellers", "indexes": ["email"]}
