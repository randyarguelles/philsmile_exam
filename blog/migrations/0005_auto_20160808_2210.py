# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160808_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 8, 14, 10, 32, 97104, tzinfo=utc)),
        ),
    ]
