# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-02 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20180102_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatemessage',
            name='dialog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='forum.Dialog'),
        ),
    ]
