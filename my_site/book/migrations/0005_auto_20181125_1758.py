# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-11-25 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_nebook'),
    ]

    operations = [
        migrations.DeleteModel(
            name='nebook',
        ),
        migrations.AddField(
            model_name='contact',
            name='place_job',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
