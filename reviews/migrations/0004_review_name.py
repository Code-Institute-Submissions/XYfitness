# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-21 21:55
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='user review', max_length=30, verbose_name=django.contrib.auth.models.User),
        ),
    ]
