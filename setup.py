#!/usr/bin/env python

from __future__ import unicode_literals
from setuptools import setup, find_packages
import io
import os

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()

version = '0.0.1'
author = 'zbyte64'
description = "Intelligently send HTML emails in Django by generating and attaching a text alternative email"
install_requires = ['django', 'six']

setup(name='django-fiendly-email',
      version=version,
      description=description,
      long_description=README,
      classifiers=[
          # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Information Technology',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Framework :: Django'
      ],
      keywords='django email',
      author=author,
      author_email='zbyte64@gmail.com',
      url='https://github.com/zbyte64/django-fiendly-email',
      license='MIT License',
      packages=find_packages(),
      platforms=["any"],
      include_package_data=True,
      test_suite='fiendly_email.test.load_suite',
      zip_safe=False,
      install_requires=install_requires,
      )
