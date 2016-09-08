# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160908_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_late',
        ),
    ]
