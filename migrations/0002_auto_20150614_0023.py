# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plugin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aln_video',
            name='height',
            field=models.PositiveSmallIntegerField(default=450, verbose_name='height'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aln_video',
            name='movie_ratio',
            field=models.CharField(default=b'16by9', choices=[(b'16by9', b'16:9'), (b'4by3', b'4:3')], max_length=10, blank=True, help_text='video ratio choice. ', null=True, verbose_name='movie ratio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aln_video',
            name='width',
            field=models.PositiveSmallIntegerField(default=600, verbose_name='width'),
            preserve_default=True,
        ),
    ]
