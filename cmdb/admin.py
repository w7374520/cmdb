# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Servers


class ServersAdmin(admin.ModelAdmin):

    list_display = ("id", "servernum", "product", "ipaddress", "apptype", "status") 


admin.site.register(Servers, ServersAdmin)
