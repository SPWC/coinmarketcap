#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'coinmarketcap',
    version = '1.1',
    url = 'https://github.com/SPWC/coinmarketcap',
    download_url = 'https://github.com/SPWC/coinmarketcap/archive/master.zip',
    author = 'Lavell Lartey <whaleofcoinbase@gmail.com>',
    author_email='whaleofcoinbase@gmail.com',
    license = 'Apache v2.0 License',
    packages = ['coinmarketcap'],
    description = 'Python wrapper around the coinmarketcap.com API.',
    long_description = open('README.md','r').read(),
    install_requires=['requests', 'requests_cache'],
    keywords = ['cryptocurrency', 'API', 'coinmarketcap','BTC', 'Bitcoin', 'LTC', 'Litecoin', 'DOGE', 'Dogecoin', 'ETH', 'Ethereum '],
)
