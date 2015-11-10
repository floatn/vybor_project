# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='title_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title_image_small',
        ),
        migrations.AlterField(
            model_name='project',
            name='date_started',
            field=models.DateField(null=True, blank=True),
        ),
    ]
