cmsplugin_aea_video
===================

A `django CMS`_ plugin for HTML5 video using `django-filer`_ and `VideoJS`_.

Install
-------
clone::
	https://github.com/web-2u/cmsplugin-aea-video.git
	$ python manage.py makemigrations
	$ python manage.py migrate

Setup
-----
Add ``cmsplugin_aea_video`` to your ``INSTALLED_APPS``.

Video Formats
-------------

Format support between browsers is a moving target.
This plugin provides fields
for the three most common formats: MP4 (h.264), WebM, and Ogg Theora.
Wikipedia has a `table of supported formats`_ for different browsers.

You can upload your videos in some or all supported formats, depending on your
needs.

Added option insert YouTube/Vimeo video url and  responsive embed by `Bootstrap 3.3`_.

.. note::

	The plugin does not support format conversion (patches welcome!) and does
	not validate the uploaded files. You might want to educate your CMS staff
	on the particularities of HTML5 video.



.. _django CMS: https://github.com/divio/django-cms
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _VideoJS: http://www.videojs.com
.. _table of supported formats: http://en.wikipedia.org/wiki/HTML5_video#Table
.. _Bootstrap 3.3: http://getbootstrap.com/components/#responsive-embed
