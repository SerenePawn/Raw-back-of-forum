# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-20 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20180102_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_pic',
            field=models.ImageField(default='forum/static/img/default_topic_pic.jpeg', upload_to=''),
        ),
    ]