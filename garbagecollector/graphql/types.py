from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model
from garbagecollector.models import Trash


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class TrashType(DjangoObjectType):
    class Meta:
        model = Trash

