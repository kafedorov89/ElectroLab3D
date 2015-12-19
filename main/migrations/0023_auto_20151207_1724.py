# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20151207_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefield',
            name='in_course',
            field=models.NullBooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u043e\u0439'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='in_report',
            field=models.NullBooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u043e\u0442\u0447\u0435\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='max_right',
            field=models.DecimalField(default=0, null=True, verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='min_right',
            field=models.DecimalField(default=0, null=True, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435', max_digits=14, decimal_places=4),
        ),
    ]
