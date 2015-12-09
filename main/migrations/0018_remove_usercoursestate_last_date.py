# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20151204_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoursestate',
            name='last_date',
        ),
    ]
