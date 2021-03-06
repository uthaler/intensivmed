# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0011_auto_20161214_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='heading_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='heading_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='heading_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='heading_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='heading_5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='heading_6',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='heading_7',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text4',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text5',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text6',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text7',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text8',
            field=models.TextField(null=True),
        ),
    ]
