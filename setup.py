#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages
from tweepy import __version__

setup(name="pystp",
		version=__version__,
		license="MIT",
		author="Dae-seon Moon",
		author_email="daeseonmoon@gmail.com",
		url="http://github.com/seanmoon80/pystp",
		packages=find_packages(exclude=['tests']),
		keywords="SolidTrustPay library",
		zip_safe=True)
