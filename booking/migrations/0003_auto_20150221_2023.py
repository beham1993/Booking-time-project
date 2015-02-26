# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_person_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='data',
            new_name='date',
        ),
    ]
