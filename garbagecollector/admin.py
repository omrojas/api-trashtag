from django.contrib import admin
from .models import Organization, Trash


admin.site.register(Trash)
admin.site.register(Organization)
