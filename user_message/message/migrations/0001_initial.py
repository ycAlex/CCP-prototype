# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-29 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.IntegerField(verbose_name='from')),
                ('to_user', models.IntegerField(verbose_name='to')),
                ('contents', models.CharField(default='', max_length=200, verbose_name='contents of message')),
                ('create_time', models.DateTimeField()),
            ],
        ),
    ]
