#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @FileName      : setup
# @Time          : 2023-11-20 09:55:40
# @Author        : zhangchao
# @description   :
"""

import ast
import os
import re
import sys

from archeryPy import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

# Publish helper
if sys.argv[-1] == 'build':
    os.system('python setup.py sdist bdist_wheel')
    sys.exit(0)

if sys.argv[-1] == 'install':
    os.system('python setup.py sdist --formats=zip')
    sys.exit(0)

setup(
    name='ArcheryPy',
    packages=['archeryPy'],
    version=version,
    description='Python library enumerating the Archery tool RESTFul API endpoints.',
    long_description=readme,
    author='wensaus',
    author_email='wensau@163.com',
    url='https://github.com/wensaus/ArcheryPy',
    license='MIT License',
    zip_safe=True,
    install_requires=['requests'],
    keywords=['pyArchery', 'api'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
    ]
)
