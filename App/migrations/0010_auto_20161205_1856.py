# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20161205_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name': 'Chapter', 'verbose_name_plural': 'Chapters'},
        ),
        migrations.AlterModelOptions(
            name='concepts',
            options={'verbose_name': 'Concept', 'verbose_name_plural': 'Concepts'},
        ),
        migrations.AlterModelOptions(
            name='sub_units',
            options={'verbose_name': 'Sub Unit', 'verbose_name_plural': 'Sub Units'},
        ),
    ]
