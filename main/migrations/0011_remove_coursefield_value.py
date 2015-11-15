# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20151115_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursefield',
            name='value',
        ),
    ]
