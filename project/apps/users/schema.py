import graph_auth.schema
import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField

from .mutations import UserMutationCreate, UserMutationUpdate, UserMutationDelete
from .types import UserType


class Mutations(graph_auth.schema.Mutation, graphene.ObjectType):
    user_create = UserMutationCreate.Field()
    user_update = UserMutationUpdate.Field()
    user_delete = UserMutationDelete.Field()


class Query(graph_auth.schema.Query, graphene.ObjectType):
    node = Node.Field()
    users = MongoengineConnectionField(UserType)


schema = graphene.Schema(query=Query, mutation=Mutations, types=[UserType])
