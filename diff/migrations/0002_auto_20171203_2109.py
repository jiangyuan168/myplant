# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interfacemodel',
            options={'ordering': ['-create_time']},
        ),
        migrations.AddField(
            model_name='interfacemodel',
            name='process',
            field=models.CharField(default=b'0', max_length=10, blank=True),
        ),
    ]
