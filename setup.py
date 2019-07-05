#!/usr/bin/env python
from setuptools import setup

setup(
    name='pi-welcome',
    version='0.1.0',
    description='A morning information dump including MBTA predictions, '
    'Weather, etc.',
    author='Kofi Collins-Sibley',
    author_email='colko818@gmail.com',
    url='https://github.com/kcollinssibley/pi-welcome',
    license='MIT',
    packages=['src'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask>=1.1.0,<2.0'
    ],
    entry_points={
        'console_scripts': [
            'app = src.app:main'
        ]
    }
)
