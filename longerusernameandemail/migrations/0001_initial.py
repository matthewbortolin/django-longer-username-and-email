# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.AlterField('auth_user', 'email', models.CharField(max_length=254)),
        migrations.AlterField('auth_user', 'username', models.CharField(max_length=254))
    ]
