#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# from distutils.core import setup
from setuptools import setup, find_packages
from tuya_connector import __version__

tests_require = []


def requirements():
    with open('requirements.txt', 'r') as fileobj:
        requirements = [line.strip() for line in fileobj]
        return requirements


with open("README.md", "r", encoding="utf-8") as fh:
    doc_long_description = fh.read()


setup(
    name='tuya-connector-python',
    url='https://github.com/tuya/tuya-connector-python',
    author="Tuya Inc.",
    author_email='developer@tuya.com',
    keywords='tuya iot cloud sdk python',
    long_description=doc_long_description,
    long_description_content_type="text/markdown",
    description='The `tuya-connector-python` SDK is desinged to support open APIs and Pulsar Messages provided by Tuya.',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/tuya/tuya-connector-python/issues",
        "Changes": "https://github.com/tuya/tuya-connector-python/wiki/Tuya-Connector-Python-Release-Notes"
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    version=__version__,
    install_requires=requirements(),
    tests_require=tests_require,
    test_suite='runtests.runtests',
    extras_require={'test': tests_require},
    entry_points={'nose.plugins': []},
    packages=find_packages(),
    python_requires='>=3.0',

)
