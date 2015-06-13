# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALN_Video',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default=b'', max_length=100, verbose_name='title', blank=True)),
                ('movie_url', models.URLField(help_text='vimeo or youtube video url. Example: http://www.youtube.com/watch?v=-iJ7bs4mTUY', max_length=255, null=True, verbose_name='movie url', blank=True)),
                ('movie_ratio', models.CharField(default=b'16:9', choices=[(b'16:9', b'16by9'), (b'4:3', b'4by3')], max_length=10, blank=True, help_text='video ratio choice. ', null=True, verbose_name='movie ratio')),
                ('width', models.PositiveSmallIntegerField(default=320, verbose_name='width')),
                ('height', models.PositiveSmallIntegerField(default=240, verbose_name='height')),
                ('auto_play', models.BooleanField(default=False, verbose_name='auto play')),
                ('auto_hide', models.BooleanField(default=False, verbose_name='auto hide')),
                ('fullscreen', models.BooleanField(default=True, verbose_name='fullscreen')),
                ('loop', models.BooleanField(default=False, verbose_name='loop')),
                ('image', filer.fields.image.FilerImageField(related_name='+', blank=True, to='filer.Image', help_text='preview image file', null=True, verbose_name='image')),
                ('video_mp4', filer.fields.file.FilerFileField(related_name='+', blank=True, to='filer.File', help_text='MP4 h264 encoded video file (Safari, Chrome, IE9)', null=True, verbose_name='movie file (MP4)')),
                ('video_ogv', filer.fields.file.FilerFileField(related_name='+', blank=True, to='filer.File', help_text='ogv encoded video file (Firefox)', null=True, verbose_name='movie file (ogv)')),
                ('video_webm', filer.fields.file.FilerFileField(related_name='+', blank=True, to='filer.File', help_text='webM encoded video file (Firefox)', null=True, verbose_name='movie file (webM)')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
