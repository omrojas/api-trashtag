from django.contrib import admin

from .models import (Cleanup, Level, Organization, Trash, TrashCleanup,
                     UserMessage, UserProfile)


class CleanupAdmin(admin.ModelAdmin):
    list_display = ('user', 'creation_date')


class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cleanups')


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'operation_area', 'phone_one', 'phone_two', 'address', 'manager_name', 'manager_phone', 'manager_email', 'checked')


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'message', 'creation_date')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')


class TrashAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_date', 'image_url')


class TrashCleanupAdmin(admin.ModelAdmin):
    list_display = ('cleanup', 'trash', 'quantity')


admin.site.register(Cleanup, admin_class=CleanupAdmin)
admin.site.register(Level, admin_class=LevelAdmin)
admin.site.register(Organization, admin_class=OrganizationAdmin)
admin.site.register(UserMessage, admin_class=UserMessageAdmin)
admin.site.register(UserProfile, admin_class=UserProfileAdmin)
admin.site.register(Trash, admin_class=TrashAdmin)
admin.site.register(TrashCleanup, admin_class=TrashCleanupAdmin)

