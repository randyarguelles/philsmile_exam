# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160906_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='employee',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_late',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='project_field',
            field=models.ForeignKey(blank=True, to='blog.Project', null=True),
        ),
    ]
