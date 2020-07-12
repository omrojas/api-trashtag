from django.contrib import admin

from .models import Organization, Trash, UserMessage

admin.site.register(Trash)
admin.site.register(Organization)
admin.site.register(UserMessage)
