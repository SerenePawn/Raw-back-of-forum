# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 18:41
from __future__ import unicode_literals

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
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField(max_length=1500)),
                ('message_date', models.DateTimeField(auto_now=True)),
                ('message_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromuser', to=settings.AUTH_USER_MODEL)),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_header', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'section',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_header', models.CharField(max_length=30)),
                ('topic_text', models.TextField()),
                ('topic_rate_plus', models.IntegerField(default=0)),
                ('topic_rate_minus', models.IntegerField(default=0)),
                ('topic_pub_date', models.DateTimeField(auto_now_add=True)),
                ('topic_edit_date', models.DateTimeField(null=True)),
                ('topic_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Section')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
        migrations.CreateModel(
            name='TopicComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField(max_length=800)),
                ('comments_pub_date', models.DateTimeField(auto_now_add=True)),
                ('comments_edit_date', models.DateTimeField(null=True)),
                ('comments_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]