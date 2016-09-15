# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-26 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0003_auto_20160826_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdviserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('id_template', models.IntegerField(default=1)),
                ('id_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
    ]