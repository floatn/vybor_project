# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('title_image', models.ImageField(upload_to=b'images/projects/')),
                ('title_image_small', models.ImageField(upload_to=b'images/projects/small/')),
                ('description', models.TextField()),
                ('date_started', models.DateField(auto_now_add=True)),
                ('date_finished', models.DateField(null=True, blank=True)),
                ('appointments', models.ManyToManyField(to='news.News')),
                ('images', models.ManyToManyField(to='news.Image')),
                ('video', models.ManyToManyField(to='news.Video')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
    ]
