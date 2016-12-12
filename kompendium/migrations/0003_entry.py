# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0002_subtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompendium.Subtopic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
