import datetime

import graphene
from django.db.models import Min, Sum
from graphql_jwt.decorators import login_required

from garbagecollector.models import (Cleanup, Level, Organization, Trash,
                                     TrashCleanup, UserProfile)

from .types import (LitterByItems, OrganizationType, PickedUpLitterPerMonth,
                    TrashType, UserStatistics, UserType)


class Query(object):
    all_trashes = graphene.List(TrashType)
    all_organizations = graphene.List(OrganizationType)
    user_information = graphene.Field(UserType)
    user_statistics = graphene.Field(UserStatistics)
    picked_up_litter_per_month = graphene.List(PickedUpLitterPerMonth)
    volunteers_number = graphene.Int()
    quantity_of_litter_by_items = graphene.List(LitterByItems)

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
            user_level = profile.level

            cleanups = Cleanup.objects.filter(user=user).count()
            items_picked = TrashCleanup.objects.filter(cleanup__user=user).aggregate(Sum('quantity'))['quantity__sum']
            items_picked =  0 if items_picked is None else items_picked

            next_level = Level.objects.filter(cleanups__gt=user_level.cleanups).order_by('cleanups').first()
            next_level_name = '' if next_level is None else next_level.name
            items_to_next_level = None if next_level is None else user_level.cleanups - items_picked

            return {
                'cleanups': cleanups,
                'itemsPicked': items_picked,
                'nextLevel': next_level_name,
                'itemsToNextLevel': items_to_next_level,
                'currentLevel': user_level.name,
                'currentLevelIcon': user_level.icon_url,
            }
        except Exception as e:
            return None


    @login_required
    def resolve_picked_up_litter_per_month(self, info, **kwargs):
        try:
            now = datetime.datetime.now()
            
            return (
                TrashCleanup.objects
                .filter(cleanup__creation_date__year=now.year)
                .values_list('cleanup__creation_date__month')
                .annotate(quantity=Sum('quantity'))
            )
        except Exception as e:
            return []


    def resolve_volunteers_number(self, info, **kwargs):
        try:
            volunteers = UserProfile.objects.count()
            return volunteers
        except Exception as e:
            return None


    def resolve_quantity_of_litter_by_items(self, info, **kwargs):
        try:
            return (
                TrashCleanup.objects
                .values_list('trash__name')
                .annotate(quantity=Sum('quantity'))
            )
        except Exception as e:
            return[]
