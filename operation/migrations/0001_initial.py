# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faultevent',
            fields=[
                ('id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('instructions', models.CharField(max_length=255, verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e')),
                ('operator', models.CharField(max_length=255, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe4\xba\xba\xe5\x91\x98')),
                ('start_time', models.CharField(max_length=128, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('end_time', models.CharField(max_length=128, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u6545\u969c\u4e8b\u4ef6',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='opreadme',
            fields=[
                ('id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('detail', models.CharField(max_length=255, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe8\xaf\xb4\xe6\x98\x8e')),
                ('operator', models.CharField(max_length=64, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe4\xba\xba')),
                ('start_time', models.CharField(max_length=128, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('end_time', models.CharField(max_length=128, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u64cd\u4f5c\u8bf4\u660e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='planevent',
            fields=[
                ('id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('instructions', models.CharField(max_length=255, verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e')),
                ('principal', models.CharField(max_length=128, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba\xe5\x91\x98')),
                ('start_time', models.CharField(max_length=128, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('end_time', models.CharField(max_length=128, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name_plural': '\u8ba1\u5212\u4e8b\u4ef6',
            },
            bases=(models.Model,),
        ),
    ]
