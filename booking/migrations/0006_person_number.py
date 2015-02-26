# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20150222_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='number',
            field=models.CharField(default=2223332223L, max_length=30),
            preserve_default=False,
        ),
    ]
