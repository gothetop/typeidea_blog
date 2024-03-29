from django.contrib import admin

from config.models import Link, SiderBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ["title", "href", "status", "weight", "created_time"]
    fields = ["title", "href", "status", "weight"]


@admin.register(SiderBar, site=custom_site)
class SiderBarAdmin(BaseOwnerAdmin):
    list_display = ["title", "display_type", "content", "created_time"]
    fields = ["title", "display_type", "content", "status"]
