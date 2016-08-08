# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('duration_time', models.DecimalField(max_digits=4, decimal_places=2, null=True)),
                ('project_field', models.CharField(max_length=100)),
                ('remarks_field', models.TextField()),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
