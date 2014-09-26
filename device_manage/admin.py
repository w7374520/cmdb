# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Servers,Routers,Switch,Storage,Firewall


class ServersAdmin(admin.ModelAdmin):
    list_display = ("id", "servernum", "product", "ipaddress", "apptype", "status") 

class RoutersAdmin(admin.ModelAdmin):
    list_display = ("id", "routernum", "product", "ipaddress", "apptype", "status")
    
class SwitchAdmin(admin.ModelAdmin):
    list_display = ("id", "switchnum", "product", "ipaddress", "apptype", "status")
    
class StorageAdmin(admin.ModelAdmin):
    list_display = ("id", "storagenum", "product", "ipaddress", "apptype", "status")

class FirewallAdmin(admin.ModelAdmin):
    list_display = ("id", "fwnum", "product", "ipaddress", "apptype", "status")
    
admin.site.register(Servers, ServersAdmin)
admin.site.register(Routers, RoutersAdmin)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Firewall, FirewallAdmin)