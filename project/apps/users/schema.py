import graph_auth.schema
import graphene
from graphene.relay import Node


class Mutation(graph_auth.schema.Mutation, graphene.ObjectType):
    pass


class Query(graph_auth.schema.Query, graphene.ObjectType):
    node = Node.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
