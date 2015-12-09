# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151127_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': '\u041e\u0442\u0432\u0435\u0442', 'verbose_name_plural': '\u041e\u0442\u0432\u0435\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-name',), 'verbose_name': '\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430', 'verbose_name_plural': '\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='coursefield',
            options={'ordering': ('-course', 'number'), 'verbose_name': '\u041f\u043e\u043b\u0435 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u043e\u0439', 'verbose_name_plural': '\u041f\u043e\u043b\u044f \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0445'},
        ),
        migrations.AlterModelOptions(
            name='method',
            options={'verbose_name': '\u041c\u0435\u0442\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b', 'verbose_name_plural': '\u041c\u0435\u0442\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-course', 'number'), 'verbose_name': '\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c', 'verbose_name_plural': '\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c'},
        ),
        migrations.AlterModelOptions(
            name='workplace',
            options={'verbose_name': '\u0421\u0442\u0435\u043d\u0434', 'verbose_name_plural': '\u0421\u0442\u0435\u043d\u0434\u044b'},
        ),
        migrations.AlterModelOptions(
            name='wpparam',
            options={'verbose_name': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u0442\u0435\u043d\u0434\u0430', 'verbose_name_plural': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u0442\u0435\u043d\u0434\u0430'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='last_date',
        ),
        migrations.AddField(
            model_name='usercoursestate',
            name='last_date',
            field=models.DateTimeField(default=6, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441', to='main.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='right',
            field=models.BooleanField(default=False, verbose_name='\u042f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0432\u0435\u0440\u043d\u044b\u043c'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text_answer',
            field=models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043e\u0442\u0432\u0435\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.DurationField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(verbose_name='\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='course',
            field=models.ForeignKey(default=1, verbose_name='\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430', to='main.Course'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='in_course',
            field=models.BooleanField(default=False, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u043e\u0439'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='in_report',
            field=models.BooleanField(default=False, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u043e\u0442\u0447\u0435\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='max_right',
            field=models.DecimalField(default=0, verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='min_right',
            field=models.DecimalField(default=0, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435', max_digits=14, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='number',
            field=models.IntegerField(default=1, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='param1',
            field=models.TextField(null=True, verbose_name='\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 1', blank=True),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='param2',
            field=models.TextField(null=True, verbose_name='\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 2', blank=True),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='param3',
            field=models.TextField(null=True, verbose_name='\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 3', blank=True),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f \u043f\u043e\u043b\u044f', to='main.FieldType'),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='wp_param',
            field=models.ForeignKey(verbose_name='UID', blank=True, to='main.WpParam', null=True),
        ),
        migrations.AlterField(
            model_name='method',
            name='course',
            field=models.ForeignKey(verbose_name='\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430', to='main.Course'),
        ),
        migrations.AlterField(
            model_name='method',
            name='text_question',
            field=models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.ForeignKey(verbose_name='\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430', to='main.Course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=1, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text_question',
            field=models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='url',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='wp_type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f', to='main.WpType'),
        ),
        migrations.AlterField(
            model_name='wpparam',
            name='code',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u041a\u043e\u0434'),
        ),
        migrations.AlterField(
            model_name='wpparam',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='wpparam',
            name='workplace',
            field=models.ForeignKey(verbose_name='\u0421\u0442\u0435\u043d\u0434', to='main.Workplace'),
        ),
        migrations.AlterField(
            model_name='wpparam',
            name='wp_param_type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f', to='main.WpParamType'),
        ),
    ]
