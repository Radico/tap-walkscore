#!/usr/bin/env python3
from setuptools import setup

setup(
    name="tap_walkscore",
    version="0.1.1",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_walkscore"],
    install_requires=[
        "singer-python==5.2.0",
        'requests==2.31.0',
        "pendulum==1.2.0",
        "tap-kit @ git+https://github.com/dmzobel/tap-kit.git@main"
    ],
    dependency_links=[
        "https://github.com/dmzobel/tap-kit/tarball/main#egg=tap-kit-0.1.1",
    ],
    entry_points="""
    [console_scripts]
    tap-walkscore=tap_walkscore:main
    """,
    packages=["tap_walkscore"],
    include_package_data=True,
)
