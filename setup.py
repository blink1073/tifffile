#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.extension import Extension

with open('README.rst') as f:
    readme = f.read()

with open('tifffile/__init__.py') as f:
    text = f.read()

version = re.search("__version__ = '(.*?)'", text).groups()[0]


# See https://stackoverflow.com/a/21621689/3622042
class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)

        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False

        import numpy
        self.include_dirs.append(numpy.get_include())


ext_modules = [Extension('tifffile._tifffile', ['tifffile/_tifffile.c'])]


setup(
    name='tifffile',
    version=version,
    description='Read and write image data from and to TIFF files.',
    long_description=readme,
    author='Steven Silvester',
    author_email='steven.silvester@ieee.org',
    url='https://github.com/blink1073/tifffile',
    include_package_data=True,
    setup_requires=[
        'numpy>=1.8.2'
    ],
    install_requires=[
        'numpy>=1.8.2',
        'pathlib;python_version<"3.0"',
        'enum34;python_version<"3.0"',
        'futures; python_version == "2.7"'
    ],
    license="BSD",
    zip_safe=False,
    packages=find_packages(),
    cmdclass={
        'build_ext': build_ext
    },
    ext_modules=ext_modules,
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
