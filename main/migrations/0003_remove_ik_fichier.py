# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-24 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_ik_fichier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ik',
            name='fichier',
        ),
    ]
