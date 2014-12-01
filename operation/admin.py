# -*- coding: utf-8 -*-

from django.contrib import admin
from models import opreadme,faultevent,planevent

class opreadmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'operator', 'start_time', 'end_time')
    list_display_links = ('id', 'title','operator','start_time','end_time')
    
class faulteventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'operator', 'start_time', 'end_time')
    list_display_links = ('id', 'title', 'operator', 'start_time', 'end_time')

class planeventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'principal', 'start_time', 'end_time')
    list_display_links = ('id', 'title', 'principal', 'start_time', 'end_time')

admin.site.register(opreadme, opreadmeAdmin)
admin.site.register(faultevent,faulteventAdmin)
admin.site.register(planevent,planeventAdmin)

