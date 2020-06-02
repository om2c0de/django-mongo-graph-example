import graphene
from django.core.exceptions import ObjectDoesNotExist

from .models import BarrelRate
from .types import BarrelRateType


class BarrelRateInput(graphene.InputObjectType):
    id = graphene.ID()
    value = graphene.Float()


class BarrelRateMutationCreate(graphene.Mutation):
    barrel_rate = graphene.Field(BarrelRateType)

    @staticmethod
    def mutate(*_, barrel_rate_data=None):
        barrel_rate = BarrelRate(value=barrel_rate_data.value)
        barrel_rate.save()
        return BarrelRateMutationCreate(barrel_rate=barrel_rate)

    class Arguments:
        barrel_rate_data = BarrelRateInput(required=True)


class BarrelRateMutationUpdate(graphene.Mutation):
    barrel_rate = graphene.Field(BarrelRateType)

    @staticmethod
    def mutate(*_, barrel_rate_data=None):
        barrel_rate = BarrelRate.objects.get(id=barrel_rate_data.id)
        if barrel_rate_data.value:
            barrel_rate.value = barrel_rate_data.value
            barrel_rate.save()
        return BarrelRateMutationUpdate(barrel_rate=barrel_rate)

    class Arguments:
        barrel_rate_data = BarrelRateInput(required=True)


class BarrelRateMutationDelete(graphene.Mutation):
    success = graphene.Boolean()

    @staticmethod
    def mutate(*_, object_id=None):
        try:
            BarrelRate.objects.get(id=object_id).delete()
            success = True
        except ObjectDoesNotExist:
            success = False
        return BarrelRateMutationDelete(success=success)

    class Arguments:
        object_id = graphene.ID(required=True)
