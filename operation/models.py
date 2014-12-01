#!-*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class  opreadme(models.Model):
    title = models.CharField(max_length=128, verbose_name="标题")
    detail = models.TextField(verbose_name="操作说明")
    operator = models.CharField(max_length=64, verbose_name="操作人")
    start_time = models.CharField(max_length=128, verbose_name="开始时间")
    end_time = models.CharField(max_length=128, verbose_name="结束时间")
    
    class Meta:
        verbose_name_plural = "操作说明"
        db_table = 'operation_opreadme'
        

class faultevent(models.Model):
    title = models.CharField(max_length=128, verbose_name="标题")
    instructions = models.TextField(verbose_name="说明")
    operator = models.CharField(max_length=255, verbose_name="处理人员")
    start_time = models.CharField(max_length=128, verbose_name="开始时间")
    end_time = models.CharField(max_length=128, verbose_name="结束时间")
    
    class Meta:
        verbose_name_plural = "故障事件"
        db_table = 'operation_faultevent'
    
class planevent(models.Model):
    title = models.CharField(max_length=128, verbose_name="标题")
    instructions = models.TextField(verbose_name="说明")
    principal = models.CharField(max_length=128, verbose_name="负责人员")
    start_time = models.CharField(max_length=128, verbose_name="开始时间")
    end_time = models.CharField(max_length=128, verbose_name="结束时间")   
    
    class Meta:
        verbose_name_plural = "计划事件"
        db_table = 'operation_planevent'
        