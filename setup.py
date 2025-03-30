#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="zams-python",
    version="0.1.0",
    description="Formation Python à la Burkinabè. Apprendre Python à travers des cours, exercices et projets contextualisés.",
    author="Alban NYANTUDRE",
    author_email="nyantudrealban@gmail.com",
    url="https://github.com/anyantudre/zams-python",
    packages=find_packages(),
    install_requires=[
        "jupyter",
        "notebook",
        "matplotlib",
        "numpy",
        "pandas",
        "scikit-learn",
        "plotly",
        "nbconvert",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: French",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 