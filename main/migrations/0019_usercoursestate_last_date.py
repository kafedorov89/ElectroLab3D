# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_usercoursestate_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercoursestate',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
