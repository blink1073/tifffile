#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
import numpy
import re


with open('README.rst') as f:
    readme = f.read()

with open('tifffile.py') as f:
    text = f.read()

version = re.search("__version__ = '(.*?)'", text).groups()[0]


setup(
    name='tifffile',
    version=version,
    description='Read and write image data from and to TIFF files.',
    long_description=readme,
    author='Steven Silvester',
    author_email='steven.silvester@ieee.org',
    url='https://github.com/blink1073/tifffile',
    py_modules=['tifffile'],
    include_package_data=True,
    ext_modules=[Extension('_tifffile',
                           ['tifffile.c'],
                           include_dirs=[numpy.get_include()])],
    requires=['numpy (>=1.8.2)'],
    license="BSD",
    zip_safe=False,
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
