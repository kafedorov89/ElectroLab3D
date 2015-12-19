# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20151206_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefield',
            name='in_course',
            field=models.BooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u043e\u0439'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='in_report',
            field=models.BooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u043e\u0442\u0447\u0435\u0442\u0435'),
        ),
    ]
