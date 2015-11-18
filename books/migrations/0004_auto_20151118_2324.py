# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20151118_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='price',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('exp', 'expense'), ('inc', 'income')], max_length=3, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
