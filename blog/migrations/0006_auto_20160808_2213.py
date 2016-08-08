# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160808_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='log_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
