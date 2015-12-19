# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20151207_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefield',
            name='number',
            field=models.IntegerField(default=1, null=True, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
    ]
