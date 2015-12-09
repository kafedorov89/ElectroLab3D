# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20151204_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoursestate',
            name='last_date',
            field=models.DateTimeField(),
        ),
    ]
