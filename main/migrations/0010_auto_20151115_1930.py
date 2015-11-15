# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_coursefieldparam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wpaction',
            name='workplace',
        ),
        migrations.RemoveField(
            model_name='wpaction',
            name='wp_param',
        ),
        migrations.RemoveField(
            model_name='wppreset',
            name='workplace',
        ),
        migrations.RemoveField(
            model_name='wppreset',
            name='wp_param',
        ),
        migrations.RemoveField(
            model_name='wpuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wpuser',
            name='workplace',
        ),
        migrations.RemoveField(
            model_name='wpuser',
            name='wp_param',
        ),
        migrations.DeleteModel(
            name='WpAction',
        ),
        migrations.DeleteModel(
            name='WpPreset',
        ),
        migrations.DeleteModel(
            name='WpUser',
        ),
    ]
