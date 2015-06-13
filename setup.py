# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

install_requires = [
    'django-cms==3.1.0',
    'django-sekizai',
    'django-filer==0.9.11',
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-aea-video",
    version = "0.1",
    url = 'https://github.com/piquadrat/cmsplugin-filer-html5video',
    license = 'BSD',
    description = "video plugin for django-cms v.3.1 and django-filer, using VideoJS",
    long_description = read('README.rst'),
    author = 'AEA Ltd.',
    author_email = 'mailsender.web.2u@gmail.com',
    packages = find_packages(),
    install_requires = install_requires,
    classifiers = [
        'Development Status :: 1 - Beta',
        'Framework :: Django 1.7.8, django-cms 3.1.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        ],
    include_package_data=True,
    zip_safe = False
)