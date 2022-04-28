from django.contrib import admin
from django_grapesjs.admin import GrapesJsAdminMixin
from .models import blogs


@admin.register(blogs)
class ExampleAdmin(GrapesJsAdminMixin, admin.ModelAdmin):
    pass