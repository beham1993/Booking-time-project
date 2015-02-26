# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(unique=True, max_length=128)),
                ('last_name', models.CharField(max_length=30)),
                ('organization_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('number', models.IntegerField(default=0)),
                ('data', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
