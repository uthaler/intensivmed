# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0018_auto_20161219_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='entry',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='entry',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
