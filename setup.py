#!/usr/bin/env python
# vim: set encoding=utf-8

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), 'r').read()

setup(
    name = "uniquepath",
    version = "1.0",
    author = "Jérôme Lecomte",
    author_email = "jlecomte1972@yahoo.com",
    description = 'Simple utility to remove duplicate and manipulate PATH-like environment variables (e.g. LD_LIBRARY_PATH, MANPATH).',
    license = "MIT",
    keywords = "path environment variable manipulation",
    url = "http://github.com/elmotec/uniquepath",
    packages=[],
    long_description=read('README.rst'),
    setup_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
)

