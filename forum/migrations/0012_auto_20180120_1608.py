# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-20 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20180120_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_pic',
            field=models.ImageField(default='img/default_topic_pic.png', upload_to=''),
        ),
    ]
