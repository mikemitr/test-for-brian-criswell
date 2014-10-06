# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import test-for-brian-criswell
version = test-for-brian-criswell.__version__

setup(
    name='test-for-brian-criswell',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'test-for-brian-criswell',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['test-for-brian-criswell/manage.py'],
)