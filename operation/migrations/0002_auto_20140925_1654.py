# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faultevent',
            name='instructions',
            field=models.TextField(max_length=255, verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e'),
        ),
        migrations.AlterField(
            model_name='opreadme',
            name='detail',
            field=models.TextField(max_length=255, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe8\xaf\xb4\xe6\x98\x8e'),
        ),
        migrations.AlterField(
            model_name='planevent',
            name='instructions',
            field=models.TextField(max_length=255, verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e'),
        ),
    ]
