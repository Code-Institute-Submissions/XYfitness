# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-26 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200426_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(max_length=40, verbose_name='Town'),
        ),
    ]
