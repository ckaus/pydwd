#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages

except ImportError as error:
    raise ImportError(error)

setup(
    name='pydwd',
    version='1.0.0',
    url='https://github.com/ckaus/pydwd',
    download_url='https://github.com/ckaus/pydwd/tarball/1.0.0',
    author='ckaus',
    author_email='christian.kaus@fu-berlin.de',
    description='Python library for crawling weather data of Germany.',
    long_description='''PyDWD crawl weather data from german weather stations.
    The weather data are provided by Deutscher Wetterdienst.''',
    license='MIT',
    packages=find_packages(),
    package_data={'pydwd.utils': ['language.cfg']},
    include_package_data=True,
    keywords=['dwd', 'weather', 'crawler'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
