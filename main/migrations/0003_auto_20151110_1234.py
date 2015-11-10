# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CourseGroupField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('course', models.ForeignKey(to='main.Course')),
            ],
        ),
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserFieldParam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=200)),
                ('field', models.ForeignKey(to='main.CourseField')),
            ],
        ),
        migrations.AddField(
            model_name='coursefield',
            name='group',
            field=models.ForeignKey(to='main.CourseGroupField'),
        ),
        migrations.AddField(
            model_name='coursefield',
            name='type',
            field=models.ForeignKey(to='main.FieldType'),
        ),
    ]
