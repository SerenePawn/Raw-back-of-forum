# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-20 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_auto_20180120_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='height',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='topic_pic',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='width',
        ),
    ]
