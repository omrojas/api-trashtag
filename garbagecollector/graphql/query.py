import graphene
from graphql_jwt.decorators import login_required

from garbagecollector.models import Organization, Trash

from .types import OrganizationType, TrashType


class Query(object):
    all_trashes = graphene.List(TrashType)
    all_organizations = graphene.List(OrganizationType)

    @login_required
    def resolve_all_trashes(self, info, **kwargs):
        try:
            return Trash.objects.all()
        except Exception as e:
            return []
   
    def resolve_all_organizations(self, info, **kwargs):
        try:
            return Organization.objects.filter(checked=True)
        except Exception as e:
            return []

