# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slides',
            options={'verbose_name': 'Slide', 'verbose_name_plural': 'Slides'},
        ),
    ]
