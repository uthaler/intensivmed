# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-14 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0023_auto_20180309_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_tags',
            field=models.ManyToManyField(to='kompendium.Tag'),
        ),
    ]
