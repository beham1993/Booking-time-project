# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20150221_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='number',
        ),
        migrations.RemoveField(
            model_name='person',
            name='time',
        ),
    ]
