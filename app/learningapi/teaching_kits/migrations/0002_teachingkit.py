# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0002_author'),
        ('teaching_kits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, help_text='URL to a regular quality image.', max_length=500, null=True)),
                ('image_retina_url', models.URLField(blank=True, help_text='URL to a retina quality image.', max_length=500, null=True)),
                ('authors', models.ManyToManyField(blank=True, related_name='teaching_kits', to='authors.Author')),
            ],
        ),
    ]
