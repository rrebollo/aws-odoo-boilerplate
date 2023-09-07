# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('VERSION') as fd:
    version = fd.read().strip()

setup(
    name="odoo-aws",
    version=version,
    description="project description",
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    author="Author...",
    author_email="email...",
    url="url...",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved',
        'License :: OSI Approved :: '
        'GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
