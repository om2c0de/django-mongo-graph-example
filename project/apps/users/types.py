from graphene import relay
from graphene_mongo import MongoengineObjectType
from .models import User


class UserType(MongoengineObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )
