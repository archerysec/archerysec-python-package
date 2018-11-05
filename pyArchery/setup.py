#!/usr/bin/env python

import os
import sys

from archery import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.md', 'r') as f:
    readme = f.read()

# Publish helper
if sys.argv[-1] == 'build':
    os.system('python pyArchery/setup.py sdist bdist_wheel')
    sys.exit(0)

if sys.argv[-1] == 'install':
    os.system('python pyArchery/setup.py sdist --formats=zip')
    sys.exit(0)

setup(
    name='pyArchery',
    packages=[
        'archery',

    ],
    version=version,
    description='Python library enumerating the Archery Tool RESTFul API endpoints.',
    long_description=readme,
    author='Anand Tiwari',
    author_email='anandtiwarics@gmail.com',
    url='https://github.com/archerysec/',
    download_url='',
    license='MIT License',
    zip_safe=True,
    install_requires=['requests'],
    keywords=['pyArchery', 'api', 'security', 'software', 'ArcherySec'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
    ]
)
