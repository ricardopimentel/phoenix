# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-30 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20181130_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtualizacao',
            name='arquitetura',
        ),
    ]
