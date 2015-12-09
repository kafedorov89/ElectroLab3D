# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_standtask_data_standtask_state_training_log_training_param_state_training_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standtask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standtask_name', models.CharField(max_length=200)),
                ('conn_json', models.TextField()),
                ('rope_json', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Standtask_data',
        ),
        migrations.AddField(
            model_name='training_log',
            name='training_name',
            field=models.CharField(default=6, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training_param_state',
            name='session_id',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training_param_state',
            name='training_id',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='standtask_state',
            name='standtask_id',
            field=models.ForeignKey(to='main.Standtask'),
        ),
    ]
