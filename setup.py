#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from ast import parse


name = 'py2nb'
# See http://stackoverflow.com/questions/2058802
with open('py2nb/__init__.py') as f:
    version = parse(next(filter(
        lambda line: line.startswith('__version__'),
        f))).body[0].value.s

py_modules = [name]

longdesc = \
"""
py2nb is a small utility for turning python scripts into jupyter notebooks and
convert module-level multiline (triple quote) string literals into markdown
cells.
"""

setup(
    name             = name,
    version          = version,
    py_modules       = py_modules,
    description      = 'py2nb: convert python script to Jupyter notebook',
    long_description = longdesc,
    keywords         = ['Jupyter notebook'],
    platforms        = 'Any',
    license          = 'BSD',
    url              = 'https://github.com/bwohlberg/py2nb',
    author           = 'Siu Kwan Lam',
    author_email     = None,
    maintainer       = 'Brendt Wohlberg',
    maintainer_email = 'brendt@ieee.org',
    setup_requires   = [],
    tests_require    = ['pytest', 'pytest-runner'],
    install_requires = ['nbformat'],
    extras_require   = {
        'tests': ['pytest', 'pytest-runner']},
    classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities',
    ],
    zip_safe = True
)
