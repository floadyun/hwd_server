# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-03 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
