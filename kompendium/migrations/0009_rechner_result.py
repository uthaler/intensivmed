# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0008_rechner'),
    ]

    operations = [
        migrations.AddField(
            model_name='rechner',
            name='result',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
