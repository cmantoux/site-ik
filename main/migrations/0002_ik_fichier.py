# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-24 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ik',
            name='fichier',
            field=models.FileField(default=None, upload_to=b''),
        ),
    ]