# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-16 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='imagem',
            field=models.ImageField(default='uploads/default.png', upload_to='uploads/', verbose_name='Logotipo'),
        ),
    ]
