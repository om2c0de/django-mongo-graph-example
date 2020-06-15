from mongoengine import Document
from mongoengine.fields import StringField, ObjectIdField


class User(Document):
    ID = ObjectIdField()
    first_name = StringField()
    last_name = StringField()

    meta = {"collection": "user"}
