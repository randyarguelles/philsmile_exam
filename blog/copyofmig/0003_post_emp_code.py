# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150903_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='emp_code',
            field=models.CharField(unique=True, default='----', max_length=4),
        ),
    ]
