# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cake_dessert_bar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='title',
        ),
        migrations.RemoveField(
            model_name='cookie',
            name='title',
        ),
        migrations.RemoveField(
            model_name='dessert_bar',
            name='title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Cake',
        ),
        migrations.DeleteModel(
            name='Cookie',
        ),
        migrations.DeleteModel(
            name='Dessert_Bar',
        ),
    ]
