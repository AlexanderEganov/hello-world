# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-11-26 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20181125_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='sex',
            new_name='gender',
        ),
    ]
