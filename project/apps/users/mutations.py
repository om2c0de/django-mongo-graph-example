import graphene
from django.core.exceptions import ObjectDoesNotExist

from .models import User
from .types import UserType


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    value = graphene.Float()


class UserMutationCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(*_, user_data=None):
        user = User(first_name=user_data.first_name, last_name=user_data.last_name)
        user.save()
        return UserMutationCreate(user=user)

    class Arguments:
        user_data = UserInput(required=True)


class UserMutationUpdate(graphene.Mutation):
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(*_, user_data=None):
        user = User.objects.get(id=user_data.id)
        if user_data.first_name:
            user.first_name = user_data.first_name
            user.save()
        if user_data.last_name:
            user.last_name = user_data.last_name
            user.save()
        return UserMutationUpdate(user=user)

    class Arguments:
        user_data = UserInput(required=True)


class UserMutationDelete(graphene.Mutation):
    success = graphene.Boolean()

    @staticmethod
    def mutate(*_, object_id=None):
        try:
            User.objects.get(id=object_id).delete()
            success = True
        except ObjectDoesNotExist:
            success = False
        return UserMutationDelete(success=success)

    class Arguments:
        object_id = graphene.ID(required=True)
