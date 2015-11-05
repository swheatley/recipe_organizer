# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_recipe_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_directions',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(null=True, blank=True),
        ),
    ]
