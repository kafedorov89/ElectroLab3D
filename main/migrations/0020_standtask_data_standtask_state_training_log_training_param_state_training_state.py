# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_usercoursestate_last_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standtask_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standtask_name', models.CharField(max_length=200)),
                ('standtask_id', models.IntegerField()),
                ('conn_json', models.TextField()),
                ('rope_json', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Standtask_state',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('standtask_id', models.IntegerField()),
                ('user_rope_json', models.TextField()),
                ('activate', models.BooleanField()),
                ('complete', models.BooleanField()),
                ('error', models.BooleanField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Training_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('training_id', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('complete', models.BooleanField()),
                ('event_list', models.TextField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Training_param_state',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bool_value', models.BooleanField()),
                ('int_value', models.IntegerField()),
                ('float_value', models.DecimalField(default=0, max_digits=14, decimal_places=4)),
                ('string_value', models.TextField()),
                ('vector3_value', models.TextField()),
                ('vector2_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Training_state',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('training_id', models.IntegerField()),
                ('online', models.BooleanField()),
                ('activate', models.BooleanField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
