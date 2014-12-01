# -*- coding: utf-8 -*-
from django.db import models


PRODUCTS = {1:u'戴尔服务器', 2:u'超威服务器', 3:u'台式机', 4:u'其他'}
SMODELS = {1:'DELL R610', 2:"DELL R710", 3:"DELL R720", 4:u"超威标配"}

PRODUCT = [(PS,PS) for PS in PRODUCTS.values()]
SMODEL = [(PM,PM) for PM in SMODELS.values()]

class Servers(models.Model):
    servernum = models.CharField(max_length=255, unique=True, verbose_name="资产编号")
    product = models.CharField(max_length=128, verbose_name="品牌", choices=PRODUCT)
    smodel = models.CharField(max_length=128, verbose_name="型号", choices=SMODEL)
    sid = models.CharField(max_length=256, verbose_name="序列号")
    cpu = models.CharField(max_length=128, verbose_name="CPU", default="Intel Xeon E5620 @2.40GHz" )
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

    #def __unicode__(self):
    #    return u"%s " % self.id

    class Meta:
        verbose_name_plural = "服务器"
        db_table = 'servers'


class Routers(models.Model):
    routernum = models.CharField(max_length=255, unique=True, verbose_name="资产编号")
    product = models.CharField(max_length=255, verbose_name="品牌型号")
    sid = models.CharField(max_length=128, verbose_name="序列号")
    rack = models.CharField(max_length=64, verbose_name="机柜", blank=True)
    ipaddress = models.CharField(max_length=128, verbose_name="IP地址", blank=True)
    interfaces = models.CharField(max_length=128, verbose_name="端口数", blank=True)
    apptype = models.CharField(max_length=255, verbose_name="业务类型", blank=True)
    principal = models.CharField(max_length=255, verbose_name="负责人", blank=True)
    status = models.CharField(max_length=32, verbose_name="状态", blank=True)
    description = models.TextField(max_length=255, verbose_name="描述", blank=True)
    other = models.CharField(max_length=255, verbose_name="其他", blank=True)
    
    class Meta:
        verbose_name_plural = "路由器"
        db_table = 'routers'
    
    

class Switch(models.Model):
    switchnum = models.CharField(max_length=255, unique=True, verbose_name="资产编号")
    product = models.CharField(max_length=255, verbose_name="品牌")
    sid = models.CharField(max_length=128, verbose_name="序列号")
    rack = models.CharField(max_length=64, verbose_name="机柜", blank=True)
    ipaddress = models.CharField(max_length=128, verbose_name="IP地址", blank=True)
    interfaces = models.CharField(max_length=128, verbose_name="端口数", blank=True)
    apptype = models.CharField(max_length=255, verbose_name="业务类型", blank=True)
    principal = models.CharField(max_length=255, verbose_name="负责人", blank=True)
    status = models.CharField(max_length=32, verbose_name="状态", blank=True)
    description = models.TextField(max_length=255, verbose_name="描述", blank=True)
    other = models.CharField(max_length=255, verbose_name="其他", blank=True)

    class Meta:
        verbose_name_plural = "交换机"
        db_table = 'switch'


class Storage(models.Model):
    storagenum = models.CharField(max_length=255, unique=True, verbose_name="资产编号")
    product = models.CharField(max_length=255, verbose_name="品牌")
    sid = models.CharField(max_length=128, verbose_name="序列号")
    rack = models.CharField(max_length=64, verbose_name="机柜", blank=True)
    ipaddress = models.CharField(max_length=128, verbose_name="IP地址", blank=True)
    interfaces = models.CharField(max_length=128, verbose_name="端口数", blank=True)
    apptype = models.CharField(max_length=255, verbose_name="业务类型", blank=True)
    principal = models.CharField(max_length=255, verbose_name="负责人", blank=True)
    status = models.CharField(max_length=32, verbose_name="状态", blank=True)
    description = models.TextField(max_length=255, verbose_name="描述", blank=True)
    other = models.CharField(max_length=255, verbose_name="其他", blank=True)

    class Meta:
        verbose_name_plural = "存储"
        db_table = 'storage'


class Firewall(models.Model):
    fwnum = models.CharField(max_length=255, unique=True, verbose_name="资产编号")
    product = models.CharField(max_length=255, verbose_name="品牌")
    sid = models.CharField(max_length=128, verbose_name="序列号")
    rack = models.CharField(max_length=64, verbose_name="机柜", blank=True)
    ipaddress = models.CharField(max_length=128, verbose_name="IP地址", blank=True)
    interfaces = models.CharField(max_length=128, verbose_name="端口说明", blank=True)
    apptype = models.CharField(max_length=255, verbose_name="业务类型", blank=True)
    principal = models.CharField(max_length=255, verbose_name="负责人", blank=True)
    status = models.CharField(max_length=32, verbose_name="状态", blank=True)
    description = models.TextField(max_length=255, verbose_name="描述", blank=True)
    other = models.CharField(max_length=255, verbose_name="其他", blank=True)
    
    class Meta:
        verbose_name_plural = "防火墙"
        db_table = 'firewall'