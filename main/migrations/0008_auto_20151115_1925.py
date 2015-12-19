# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151115_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefield',
            name='wp_param',
            field=models.ForeignKey(to='main.WpParam', null=True),
        ),
    ]
