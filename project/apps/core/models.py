from mongoengine import Document
from mongoengine.fields import FloatField, ObjectIdField


class BarrelRate(Document):
    ID = ObjectIdField()
    value = FloatField()

    meta = {"collection": "barrel_rate"}
