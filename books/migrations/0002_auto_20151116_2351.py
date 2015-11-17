# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='created',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 11, 16, 21, 51, 54, 805686, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receipt',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 16, 21, 50, 54, 951814, tzinfo=utc)),
        ),
    ]
