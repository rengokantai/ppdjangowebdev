# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blat',
            old_name='tesxt',
            new_name='text',
        ),
    ]
