# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='workplace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='wp_action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField(default=0)),
                ('workplace', models.ForeignKey(to='main.workplace')),
            ],
        ),
        migrations.CreateModel(
            name='wp_param',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('workplace', models.ForeignKey(to='main.workplace')),
            ],
        ),
        migrations.CreateModel(
            name='wp_param_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='wp_preset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.IntegerField(default=0)),
                ('workplace', models.ForeignKey(to='main.workplace')),
                ('wp_param', models.ForeignKey(to='main.wp_param')),
            ],
        ),
        migrations.CreateModel(
            name='wp_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='wp_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=0)),
                ('workplace', models.ForeignKey(to='main.workplace')),
                ('wp_param', models.ForeignKey(to='main.wp_param')),
            ],
        ),
        migrations.AddField(
            model_name='wp_param',
            name='wp_param_type',
            field=models.ForeignKey(to='main.wp_param_type'),
        ),
        migrations.AddField(
            model_name='wp_action',
            name='wp_param',
            field=models.ForeignKey(to='main.wp_param'),
        ),
        migrations.AddField(
            model_name='workplace',
            name='wp_type',
            field=models.ForeignKey(to='main.wp_type'),
        ),
    ]
