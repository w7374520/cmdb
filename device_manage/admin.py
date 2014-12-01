# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Servers,Routers,Switch,Storage,Firewall
from django.forms import ModelForm


class ServersAdmin(admin.ModelAdmin):
    list_display = ("id", "servernum", "rack", "smodel", "ipaddress", "os", "ipmi", "apptype", "principal", "status") 
    list_display_links = ("id", "servernum", "rack", "smodel", "ipaddress", "os", "ipmi", "apptype", "principal", "status") 


class RoutersAdmin(admin.ModelAdmin):
    list_display = ("id", "routernum", "product", "rack", "ipaddress", "apptype", "status")
    list_display_links = ("id", "routernum", "product", "rack", "ipaddress", "apptype", "status")

    
class SwitchAdmin(admin.ModelAdmin):
    list_display = ("id", "switchnum", "product", "ipaddress", "apptype", "status")
    list_display_links = ("id", "switchnum", "product", "ipaddress", "apptype", "status")
    
class StorageAdmin(admin.ModelAdmin):
    list_display = ("id", "storagenum", "product", "ipaddress", "apptype", "status")
    list_display_links = ("id", "storagenum", "product", "ipaddress", "apptype", "status")

class FirewallAdmin(admin.ModelAdmin):
    list_display = ("id", "fwnum", "product", "ipaddress", "apptype", "status")
    list_display_links = ("id", "fwnum", "product", "ipaddress", "apptype", "status")


#class ServerForm(ModelForm):
#    class Meta:
#        model = Servers
#        


admin.site.register(Servers, ServersAdmin)
admin.site.register(Routers, RoutersAdmin)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Firewall, FirewallAdmin)