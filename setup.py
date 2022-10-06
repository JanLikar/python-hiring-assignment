#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='assignment',
    version='1.0',
    description='Hiring assignment',
    author='',
    author_email='',
    packages=find_packages("assignment"),
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
        ]
    }
)
