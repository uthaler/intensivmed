# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0014_auto_20161214_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
