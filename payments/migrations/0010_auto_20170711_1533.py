# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_auto_20170711_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_made',
            name='payment_date',
            field=models.DateField(),
        ),
    ]
