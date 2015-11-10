# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images/')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('title_image', models.ImageField(upload_to=b'images/news/')),
                ('title_image_small', models.ImageField(upload_to=b'images/news/small/')),
                ('images', models.ManyToManyField(to='news.Image')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.URLField()),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.ManyToManyField(to='news.Video'),
            preserve_default=True,
        ),
    ]
