#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from distutils.core import Extension
from distutils.log import warn

import re


with open('README.rst') as f:
    readme = f.read()

with open('tifffile/__init__.py') as f:
    text = f.read()

version = re.search("__version__ = '(.*?)'", text).groups()[0]


setup_args = dict(
    name='tifffile',
    version=version,
    description='Read and write image data from and to TIFF files.',
    long_description=readme,
    author='Steven Silvester',
    author_email='steven.silvester@ieee.org',
    url='https://github.com/blink1073/tifffile',
    include_package_data=True,
    requires=['numpy (>=1.8.2)', 'setuptools'],
    license="BSD",
    zip_safe=False,
    packages=find_packages(),
    keywords='tifffile',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        "Programming Language :: C",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)

try:
    import numpy
    setup_args['ext_modules'] = [
        Extension('tifffile._tifffile',
                  ['tifffile/_tifffile.c'],
                  include_dirs=[numpy.get_include()])
    ]
except ImportError:
    warn('Cannot build the extension module without numpy')


setup(**setup_args)
