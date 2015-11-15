# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_coursefield_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursefieldparam',
            name='course_field',
        ),
        migrations.AddField(
            model_name='coursefield',
            name='param1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='param2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='param3',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='CourseFieldParam',
        ),
    ]
