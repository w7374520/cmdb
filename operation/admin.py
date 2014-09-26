# -*- coding: utf-8 -*-

from django.contrib import admin
from models import opreadme,faultevent,planevent

class opreadmeAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'operator', 'start_time', 'end_time')

class faulteventAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructions', 'operator', 'start_time', 'end_time')

class planeventAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructions', 'principal', 'start_time', 'end_time')


admin.site.register(opreadme, opreadmeAdmin)
admin.site.register(faultevent,faulteventAdmin)
admin.site.register(planevent,planeventAdmin)

