from graphene import relay
from graphene_mongo import MongoengineObjectType
from .models import BarrelRate


class BarrelRateType(MongoengineObjectType):
    class Meta:
        model = BarrelRate
        interfaces = (relay.Node, )
