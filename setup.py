# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="gym-renju",
    version="0.1.0",
    description="Renju Game Gym Environment",
    license="MIT",
    author="kkbnart",
    packages=find_packages(),
    keywords='gym renju reinforcement learning',
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=['gym', 'pytest', 'parameterized'],
)
