# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0002_auto_20171107_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='bonus',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
