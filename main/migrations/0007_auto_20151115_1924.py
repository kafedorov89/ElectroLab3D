# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151115_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefield',
            name='value',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='wp_param',
            field=models.ForeignKey(default=1, to='main.WpParam', null=True),
        ),
    ]
