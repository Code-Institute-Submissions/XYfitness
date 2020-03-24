# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-24 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_shirt_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shirt_size',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('P', 'Plan'), ('A', 'Apparel')], default='P', max_length=30),
        ),
    ]
