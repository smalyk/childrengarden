# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20170711_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='total_payed',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Всего внесено'),
        ),
    ]
