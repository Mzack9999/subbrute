#!/usr/bin/env python
import os
from setuptools import setup, find_packages


long_description = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.md'
    )
).read()


setup(
    name='SubBrute',
    version='2.1',
    license='LICENSE',
    url='https://github.com/TheRook/subbrute',
    description='Subdomain enumeration tool.',
    long_description=long_description,
    packages=find_packages('.', exclude=["dnslib"]),
    py_modules=["subbrute"],
    data_files=[('', ['names.txt', 'names_small.txt', 'resolvers.txt'])],
    install_requires=['dnslib'],
    entry_points={
        'console_scripts': [
            'subbrute = subbrute:main',
        ]
    },
    keywords=['dns', 'subdomain', 'enumeration']
)