# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_adviserinvitations'),
    ]

    operations = [
        migrations.AddField(
            model_name='adviseruser',
            name='id_company',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]