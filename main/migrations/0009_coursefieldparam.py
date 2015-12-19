# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151115_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFieldParam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.TextField(null=True)),
                ('course_field', models.ForeignKey(to='main.CourseField')),
            ],
        ),
    ]
