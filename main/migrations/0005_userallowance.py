# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAllowance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('construct', models.BooleanField(default=False)),
                ('course_start', models.BooleanField(default=False)),
                ('report', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='main.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
