# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0002_skill'),
        ('competencies', '0002_competency'),
        ('weblitskills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebLitSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('short_name', models.CharField(max_length=100)),
                ('competencies', models.ManyToManyField(blank=True, related_name='weblit_skills', to='competencies.Competency')),
                ('skills', models.ManyToManyField(blank=True, related_name='weblit_skills', to='skills.Skill')),
            ],
        ),
    ]
