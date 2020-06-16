import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField

from .mutations import BarrelRateMutationCreate, BarrelRateMutationUpdate, BarrelRateMutationDelete
from .types import BarrelRateType


class Mutations(graphene.ObjectType):
    barrel_rate_create = BarrelRateMutationCreate.Field()
    barrel_rate_update = BarrelRateMutationUpdate.Field()
    barrel_rate_delete = BarrelRateMutationDelete.Field()


class Query(graphene.ObjectType):
    node = Node.Field()
    barrel_rates = MongoengineConnectionField(BarrelRateType)


# schema = graphene.Schema(query=Query, mutation=Mutations, types=[BarrelRateType])
