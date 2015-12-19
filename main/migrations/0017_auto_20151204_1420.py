# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20151204_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standtaskstate',
            name='stand_task',
        ),
        migrations.RemoveField(
            model_name='standtaskstate',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trainingeventlog',
            name='traning',
        ),
        migrations.RemoveField(
            model_name='trainingeventlog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='traininglist',
            name='traning',
        ),
        migrations.DeleteModel(
            name='StandTask',
        ),
        migrations.DeleteModel(
            name='StandTaskState',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
        migrations.DeleteModel(
            name='TrainingEventLog',
        ),
        migrations.DeleteModel(
            name='TrainingList',
        ),
    ]
