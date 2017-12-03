# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diff', '0002_auto_20171203_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interfacemodel',
            old_name='process',
            new_name='status',
        ),
    ]
