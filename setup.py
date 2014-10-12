#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
import numpy

readme = open('README.rst').read()


setup(
    name='tifffile',
    version='0.1.0',
    description='Read and write image data from and to TIFF files.',
    long_description=readme,
    author='Steven Silvester',
    author_email='steven.silvester@ieee.org',
    url='https://github.com/blink1073/tifffile',
    packages=['tifffile'],
    package_dir={'tifffile': 'tifffile'},
    include_package_data=True,
    ext_modules=[Extension('tifffile/_tifffile',
                           ['tifffile/tifffile.c'],
                           include_dirs=[numpy.get_include()])],
    requires=['numpy (>=1.8.2)'],
    license="BSD",
    zip_safe=False,
    keywords='tifffile',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
