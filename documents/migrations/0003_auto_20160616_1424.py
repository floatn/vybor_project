# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20160616_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='description',
            field=models.CharField(max_length=35),
        ),
    ]
