# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0010_auto_20160413_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='age',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='result',
            name='bib',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='result',
            name='pace',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='result',
            name='splits',
            field=models.CharField(default='', max_length=400),
        ),
    ]
