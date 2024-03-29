import graphene
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType

from garbagecollector.models import Organization, Trash


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')


class TrashType(DjangoObjectType):
    class Meta:
        model = Trash


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = ('id', 'name')


class TrashQuantity(graphene.InputObjectType):
    trashId = graphene.Int(required=True)
    quantity = graphene.Int(required=True)


class UserStatistics(graphene.ObjectType):
    cleanups = graphene.Int()
    items_picked = graphene.Int()
    items_to_next_level = graphene.Int()
    next_level = graphene.String()
    current_level = graphene.String()
    current_level_icon = graphene.String()

    def resolve_cleanups(statistics, info):
        return statistics['cleanups']

    def resolve_items_picked(statistics,info):
        return statistics['itemsPicked']

    def resolve_items_to_next_level(statistics,info):
        return statistics['itemsToNextLevel']

    def resolve_next_level(statistics,info):
        return statistics['nextLevel']

    def resolve_current_level(statistics,info):
        return statistics['currentLevel']

    def resolve_current_level_icon(statistics,info):
        return statistics['currentLevelIcon']


class PickedUpLitterPerMonth(graphene.ObjectType):
    month = graphene.Int()
    quantity = graphene.Int()
    
    def resolve_month(data, info):
        return data[0]

    def resolve_quantity(data, info):
        return data[1]


class LitterByItems(graphene.ObjectType):
    garbage = graphene.String()
    quantity = graphene.Int()
    
    def resolve_garbage(data, info):
        return data[0]

    def resolve_quantity(data, info):
        return data[1]