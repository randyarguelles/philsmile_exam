# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160808_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='log_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
