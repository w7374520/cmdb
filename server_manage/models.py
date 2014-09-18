# -*- coding: utf-8 -*-

from django.db import models


class Servers(models.Model):
    id = models.IntegerField(primary_key=True, max_length=128)
    servernum = models.CharField(max_length=255, unique=True, verbose_name="资产编号")
    product = models.CharField(max_length=128, verbose_name="品牌")
    sid = models.CharField(max_length=128, verbose_name="序列号")
    cpu = models.CharField(max_length=128, verbose_name="CPU")
    memory = models.CharField(max_length=128, verbose_name="内存")
    disk = models.CharField(max_length=128, verbose_name="硬盘")
    os = models.CharField(max_length=128, verbose_name="操作系统", blank=True)
    rack = models.CharField(max_length=64, verbose_name="机柜", blank=True)
    ipaddress = models.CharField(max_length=128, verbose_name="IP地址", blank=True)
    ipmi = models.CharField(max_length=128, verbose_name="IPMI地址", blank=True)
    mac = models.CharField(max_length=255, verbose_name="MAC地址", blank=True)
    apptype = models.CharField(max_length=255, verbose_name="业务类型", blank=True)
    principal = models.CharField(max_length=255, verbose_name="负责人")
    status = models.CharField(max_length=32, verbose_name="状态")
    description = models.TextField(max_length=255, verbose_name="描述", blank=True)
    other = models.CharField(max_length=255, verbose_name="其它", blank=True)

    def __unicode__(self):
        return u"%s " % self.id

    class Meta:
        verbose_name_plural = "服务器信息"


class Routers(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    routernum = models.CharField(max_length=255, unique=True)
    product = models.CharField(max_length=255)
    sid = models.CharField(max_length=128)
    ipaddress = models.CharField(max_length=128)
    interfaces = models.CharField(max_length=128)
    apptype = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    description = models.TextField(max_length=255)
    other = models.CharField(max_length=255)


class Switch(models.Model):
    id = models.IntegerField(primary_key=True, max_length=128)
    switchnum = models.CharField(max_length=255, unique=True)
    product = models.CharField(max_length=255)
    sid = models.CharField(max_length=128)
    ipaddress = models.CharField(max_length=128)
    interfaces = models.CharField(max_length=128)
    apptype = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    description = models.TextField(max_length=255)
    other = models.CharField(max_length=255)


class Storage(models.Model):
    id = models.IntegerField(primary_key=True, max_length=128)
    storagenum = models.CharField(max_length=255, unique=True)
    product = models.CharField(max_length=255)
    sid = models.CharField(max_length=128)
    ipaddress = models.CharField(max_length=128)
    interfaces = models.CharField(max_length=128)
    apptype = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    description = models.TextField(max_length=255)
    other = models.CharField(max_length=255)


class Firewall(models.Model):
    id = models.IntegerField(primary_key=True, max_length=128)
    fwnum = models.CharField(max_length=255, unique=True)
    product = models.CharField(max_length=255)
    sid = models.CharField(max_length=128)
    ipaddress = models.CharField(max_length=128)
    interfaces = models.CharField(max_length=128)
    apptype = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    description = models.TextField(max_length=255)
    other = models.CharField(max_length=255)
