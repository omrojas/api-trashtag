import graphene
from django.db.models import Min, Sum
from graphql_jwt.decorators import login_required

from garbagecollector.models import Level, Organization, Trash, TrashCleanup

from .types import OrganizationType, TrashType, UserStatistics, UserType


class Query(object):
    all_trashes = graphene.List(TrashType)
    all_organizations = graphene.List(OrganizationType)
    user_information = graphene.Field(UserType)
    user_statistics = graphene.Field(UserStatistics)

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

    @login_required
    def resolve_user_information(self, info, **kwargs):
        try:
            user = info.context.user
            return user
        except Exception as e:
            return None

    @login_required
    def resolve_user_statistics(self, info, **kwargs):
        try:
            user = info.context.user
            cleanups = TrashCleanup.objects.filter(cleanup__user=user).count()
            itemsPicked = TrashCleanup.objects.filter(cleanup__user=user).aggregate(Sum('quantity'))['quantity__sum']
            nextLevelCleanups= Level.objects.filter(cleanups__gte=itemsPicked).aggregate(Min('cleanups'))['cleanups__min']
            itemsToNextLevel = 0

            if nextLevelCleanups is not None:
                itemsToNextLevel = nextLevelCleanups - itemsPicked

            return {
                'cleanups': cleanups,
                'itemsPicked': itemsPicked,
                'itemsToNextLevel': itemsToNextLevel
            }
        except Exception as e:
            return None
