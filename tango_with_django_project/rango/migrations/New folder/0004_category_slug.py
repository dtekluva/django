# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
