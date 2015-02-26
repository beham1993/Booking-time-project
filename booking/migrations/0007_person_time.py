# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_person_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='time',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
