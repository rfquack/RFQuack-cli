#!/usr/bin/env python

from setuptools import setup

DEPENDENCIES = open('requirements.pip', 'r').read().split('\n')
README = open('README.md', 'r').read()

setup(
    name='rfquack',
    version='0.0.1',
    description='Python library and command-line utility for RFQuack dongles',
    long_description=README,
    author='Federico Maggi',
    author_email='fede@maggi.cc',
    url='http://github.com/rfquack/RFQuack-cli',
    packages=['rfquack'],
    entry_points={'console_scripts': ['rfquack=rfquack.cli:main']},
    install_requires=DEPENDENCIES,
    keywords=['rf', 'radio'],
    classifiers=[
      'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
