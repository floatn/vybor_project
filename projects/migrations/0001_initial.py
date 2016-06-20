# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '__first__'),
        ('news', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_finished', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=b'images/projects/')),
                ('appointments', models.ManyToManyField(blank=True, to='news.News')),
                ('video', models.ManyToManyField(blank=True, to='video.Video')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
