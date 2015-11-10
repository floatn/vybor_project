# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151103_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='appointments',
            field=models.ManyToManyField(to=b'news.News', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(to=b'news.Image', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.ManyToManyField(to=b'news.Video', null=True, blank=True),
        ),
    ]
