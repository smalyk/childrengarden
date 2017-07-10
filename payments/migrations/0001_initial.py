# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 12:05
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('discount', models.BooleanField(default=False, verbose_name='Льгота')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ФИО родителя')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_made',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('payment_date', models.DateField(auto_now=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ФИО родителя')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_needed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reckoning', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('deadline', models.DateField(default=datetime.datetime.now, verbose_name='Срок сдачи')),
                ('discount', models.BooleanField(default=False, verbose_name='Льгота')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Category', verbose_name='Категория')),
            ],
        ),
    ]