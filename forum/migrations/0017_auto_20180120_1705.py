# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-20 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0016_auto_20180120_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_pic',
            field=models.ImageField(height_field='height', upload_to='', width_field='width'),
        ),
    ]
