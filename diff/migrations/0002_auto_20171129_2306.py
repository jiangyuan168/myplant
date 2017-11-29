# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfacemodel',
            name='defaulturl',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='interfacemodel',
            name='testurl',
            field=models.CharField(max_length=300),
        ),
    ]
