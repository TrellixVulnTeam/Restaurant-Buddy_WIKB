# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-21 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import restaurant.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_dish_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurant.validators.validate_location]),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]