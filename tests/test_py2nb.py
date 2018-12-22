#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for py2jn module"""

import os
from tempfile import gettempdir
import pytest
import py2jn
from py2jn.__main__ import python_to_notebook


@pytest.fixture
def samplepy(fname='example.py'):
    return os.path.join('tests', fname)


@pytest.fixture
def sampleipynb(fname='example.ipynb'):
    return os.path.join('tests', fname)


def test_py2jn(samplepy, sampleipynb):
    tmpdir = gettempdir()
    outfile = os.path.join(tmpdir, 'py2jn_example.ipynb')
    python_to_notebook(input_filename=samplepy, output_filename=outfile)
    with open(os.path.join(tmpdir, 'py2jn_example.ipynb'), 'r') as outfileobj:
        outfile = outfileobj.read()
    with open(sampleipynb, 'r') as reffileobj:
        refile = reffileobj.read()
    assert outfile == refile
    os.remove(os.path.join(tmpdir, 'py2jn_example.ipynb'))


def test_str_to_str(samplepy, sampleipynb):
    with open(samplepy, 'r') as fin:
        pystr = fin.read()
    nbstr = py2jn.py_string_to_nb_string(pystr)
    nb = py2jn.nb_string_to_notebook(nbstr)
    nbstr = py2jn.write_notebook_to_string(nb)
    with open(sampleipynb, 'r') as fin:
        nbstrref = fin.read()
    assert nbstr == nbstrref
