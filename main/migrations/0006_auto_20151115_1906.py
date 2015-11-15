# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_userallowance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursegroupfield',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursefield',
            name='group',
        ),
        migrations.AddField(
            model_name='coursefield',
            name='course',
            field=models.ForeignKey(default=1, to='main.Course'),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='wp_param',
            field=models.ForeignKey(default=1, to='main.WpParam'),
        ),
        migrations.AddField(
            model_name='fieldtype',
            name='code',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='workplace',
            name='url',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='wpparam',
            name='code',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.DeleteModel(
            name='CourseGroupField',
        ),
    ]
