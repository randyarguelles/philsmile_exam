# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='log_date',
            field=models.DateTimeField(default=datetime.date(2016, 8, 8)),
        ),
    ]
