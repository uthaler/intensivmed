# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-29 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0025_auto_20180329_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='bga',
            name='blutzucker',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Glucose'),
        ),
        migrations.AddField(
            model_name='bga',
            name='bun',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='BUN'),
        ),
    ]
