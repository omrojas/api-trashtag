from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (Cleanup, Level, Organization, Trash, TrashCleanup,
                     UserMessage, UserOrganization, UserProfile)


class CleanupAdmin(ImportExportModelAdmin):
    list_display = ('user', 'creation_date',  'latitude', 'longitude')


class LevelAdmin(ImportExportModelAdmin):
    list_display = ('name', 'cleanups', 'icon_url')


class OrganizationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'operation_area', 'phone_one', 'phone_two', 'address', 'manager_name', 'manager_phone', 'manager_email', 'checked')


class UserMessageAdmin(ImportExportModelAdmin):
    list_display = ('user', 'subject', 'message', 'creation_date')


class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'level')


class TrashAdmin(ImportExportModelAdmin):
    list_display = ('name', 'creation_date', 'image_url', 'icon_url')


class TrashCleanupAdmin(ImportExportModelAdmin):
    list_display = ('cleanup', 'trash', 'quantity')


class UserOrganizationAdmin(ImportExportModelAdmin):
    list_display = ('user', 'organization')


admin.site.register(Cleanup, admin_class=CleanupAdmin)
admin.site.register(Level, admin_class=LevelAdmin)
admin.site.register(Organization, admin_class=OrganizationAdmin)
admin.site.register(UserMessage, admin_class=UserMessageAdmin)
admin.site.register(UserOrganization, admin_class=UserOrganizationAdmin)
admin.site.register(UserProfile, admin_class=UserProfileAdmin)
admin.site.register(Trash, admin_class=TrashAdmin)
admin.site.register(TrashCleanup, admin_class=TrashCleanupAdmin)

