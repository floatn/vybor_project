# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='images',
            field=models.ManyToManyField(to=b'news.Image', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.ManyToManyField(to=b'news.Video', null=True, blank=True),
        ),
    ]
