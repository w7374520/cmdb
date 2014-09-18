# -*- coding: utf-8 -*-

from django.db import models


class Servers(models.Model):
    id = models.IntegerField(primary_key=True, max_length=128)
    servernum = models.CharField(max_length=255, unique=True)
    product = models.CharField(max_length=128)
    sid = models.CharField(max_length=128)
    cpu = models.CharField(max_length=128)
    memory = models.CharField(max_length=128)
    disk = models.CharField(max_length=128)
    os = models.CharField(max_length=128)
    rack = models.CharField(max_length=64)
    ipaddress = models.CharField(max_length=128)
    ipmi = models.CharField(max_length=128)
    mac = models.CharField(max_length=255)
    apptype = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    description = models.TextField(max_length=255)
    other = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s " % self.id


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
