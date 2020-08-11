import graphene
from django.db.models import Min, Sum
from graphql_jwt.decorators import login_required

from garbagecollector.models import (Cleanup, Level, Organization, Trash,
                                     TrashCleanup, UserProfile)

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
            profile = UserProfile.objects.filter(user=user).first()
            cleanups = Cleanup.objects.filter(user=user).count()
            itemsPicked = TrashCleanup.objects.filter(cleanup__user=user).aggregate(Sum('quantity'))['quantity__sum']
            itemsPicked =  0 if itemsPicked is None else itemsPicked

            nextLevels= Level.objects.filter(cleanups__gt=itemsPicked).order_by('cleanups')
            nextLevel = nextLevels.first()
            nextLevelName =  '' if nextLevel is None else nextLevel.name
            itemsToNextLevel = 0 if nextLevel is None else nextLevel.cleanups - itemsPicked
            currentLevelName =  '' if profile.level is None else profile.level.name
            
            return {
                'cleanups': cleanups,
                'itemsPicked': itemsPicked,
                'nextLevel': nextLevelName,
                'itemsToNextLevel': itemsToNextLevel,
                'currentLevel': currentLevelName,
            }
        except Exception as e:
            return None
