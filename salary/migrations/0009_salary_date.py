# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0008_auto_20171113_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
