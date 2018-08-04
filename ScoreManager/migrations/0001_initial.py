# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-22 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('chinese', models.FloatField()),
                ('math', models.FloatField()),
                ('english', models.FloatField()),
                ('physics', models.FloatField()),
                ('chemistry', models.FloatField()),
                ('summary', models.FloatField()),
            ],
        ),
    ]