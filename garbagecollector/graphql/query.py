import graphene
from graphql_jwt.decorators import login_required
from garbagecollector.models import Trash
from .types import TrashType


class Query(object):
    all_trashes = graphene.List(TrashType)

    @login_required
    def resolve_all_trashes(self, info, **kwargs):
        try:
            return Trash.objects.all()
        except Exception as e:
            return []

