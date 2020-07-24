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
