# -*- coding: utf-8 -*-

from django.contrib import admin
from models import IdcRoom

# Register your models here.

class IdcroomAdmin(admin.ModelAdmin):
    list_display = ("id", "roomname", "rack", "localzone", "ipnet", "principal")
    list_display_links = ("id", "roomname", "rack", "localzone", "ipnet", "principal")

admin.site.register(IdcRoom,IdcroomAdmin)