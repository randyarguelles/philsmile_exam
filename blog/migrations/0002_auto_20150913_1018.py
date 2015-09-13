# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='emp_address',
            field=models.CharField(default=' ', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='emp_contact_telno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='emp_first_name',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='emp_last_name',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='emp_middle_name',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='emp_nationality',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='emp_tin_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
