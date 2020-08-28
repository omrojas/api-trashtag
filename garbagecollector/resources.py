from import_export import resources

from .models import (Cleanup, Level, Organization, Trash, TrashCleanup,
                     UserMessage, UserOrganization, UserProfile)


class CleanupResource(resources.ModelResource):
    class Meta:
        model = Cleanup


class LevelResource(resources.ModelResource):
    class Meta:
        model = Level


class OrganizationResource(resources.ModelResource):
    class Meta:
        model = Organization


class TrashResource(resources.ModelResource):
    class Meta:
        model = Trash


class TrashCleanupResource(resources.ModelResource):
    class Meta:
        model = TrashCleanup


class UserMessageResource(resources.ModelResource):
    class Meta:
        model = UserMessage


class UserOrganizationResource(resources.ModelResource):
    class Meta:
        model = UserOrganization


class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile

