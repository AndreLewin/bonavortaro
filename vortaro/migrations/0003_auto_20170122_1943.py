# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vortaro', '0002_auto_20170122_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radiko',
            old_name='radikaro',
            new_name='eraro',
        ),
    ]
