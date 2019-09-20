#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:37:16 2019

@author: malkusch
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qSMLM",
    version="19.09",
    author="Sebastian Malkusch",
    author_email="malkusch@med.uni-frankfurt.com",
    description="a package filtering compound GWAVA data sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SMLMS/filterGWAVA.git",
    packages=setuptools.find_packages(),
	install_requires=['numpy',
						'matplotlib',
						'scipy',
						'IPython',
						'ipywidgets',
						'hide_code'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
)