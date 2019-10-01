#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:37:16 2019

filterGwava

Copyright (C) 2019  Sebastian Malkusch
malkusch@med.uni-frankfurt.de

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

run with
python setup.py sdist bdist_wheel
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filterGWAVA",
    version="19.09",
    author="Sebastian Malkusch",
    author_email="malkusch@med.uni-frankfurt.com",
    description="a package filtering compound GWAVA data sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SMLMS/filterGWAVA.git",
    packages=setuptools.find_packages(),
    install_requires = ['argparse',
                        'datetime',
                        'os',
                        'pandas',
                        're'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
)