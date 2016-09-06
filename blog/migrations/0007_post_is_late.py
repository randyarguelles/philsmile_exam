# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160808_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_late',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
