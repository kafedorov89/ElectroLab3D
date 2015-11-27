# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_standtask_standtaskstate_training_trainingeventlog_traininglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefield',
            name='in_course',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='in_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='max_right',
            field=models.DecimalField(default=0, max_digits=14, decimal_places=4),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='min_right',
            field=models.DecimalField(default=0, max_digits=14, decimal_places=4),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
