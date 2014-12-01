# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class IdcRoom(models.Model):
    roomname = models.CharField(max_length=128, verbose_name="机房名称")
    rack = models.CharField(max_length=64, verbose_name = "机柜号")
    localzone = models.CharField(max_length=64, verbose_name = "地区")
    ipnet = models.CharField(max_length=128, verbose_name = "IP网段")
    principal = models.CharField(max_length=255, verbose_name="负责人")
    
    class Meta:
        verbose_name_plural = "机房"
        db_table = 'idcroom'
