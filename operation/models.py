#!-*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class  opreadme(models.Model):
    #id = models.CharField(primary_key=True, max_length=128)
    title = models.CharField(max_length=128, verbose_name="标题")
    detail = models.TextField(max_length=255, verbose_name="操作说明")
    operator = models.CharField(max_length=64, verbose_name="操作人")
    start_time = models.CharField(max_length=128, verbose_name="开始时间")
    end_time = models.CharField(max_length=128, verbose_name="结束时间")
    
    class Meta:
        verbose_name_plural = "操作说明"
        

class faultevent(models.Model):
    #id = models.CharField(primary_key=True, max_length=128)
    title = models.CharField(max_length=128, verbose_name="标题")
    instructions = models.TextField(max_length=255, verbose_name="说明")
    operator = models.CharField(max_length=255, verbose_name="处理人员")
    start_time = models.CharField(max_length=128, verbose_name="开始时间")
    end_time = models.CharField(max_length=128, verbose_name="结束时间")
    
    class Meta:
        verbose_name_plural = "故障事件"
    
class planevent(models.Model):
    #id = models.CharField(primary_key=True, max_length=128)
    title = models.CharField(max_length=128, verbose_name="标题")
    instructions = models.TextField(max_length=255, verbose_name="说明")
    principal = models.CharField(max_length=128, verbose_name="负责人员")
    start_time = models.CharField(max_length=128, verbose_name="开始时间")
    end_time = models.CharField(max_length=128, verbose_name="结束时间")   
    
    class Meta:
        verbose_name_plural = "计划事件"
        