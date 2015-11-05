# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_cookie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.ForeignKey(blank=True, to='main.Recipe', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dessert_Bar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.ForeignKey(blank=True, to='main.Recipe', null=True)),
            ],
        ),
    ]
