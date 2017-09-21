# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='inputs',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='outputs',
            field=models.FileField(default=django.utils.timezone.now, upload_to='testcases/'),
            preserve_default=False,
        ),
    ]
