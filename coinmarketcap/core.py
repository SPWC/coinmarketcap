#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import requests_cache
from pprint import pprint
import random
from retrying import retry

class Market(object):

	_session = None
	__DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v1/'
	__DEFAULT_TIMEOUT = 3

	def __init__(self, base_url = __DEFAULT_BASE_URL, request_timeout = __DEFAULT_TIMEOUT):
		self.base_url = base_url
		self.request_timeout = request_timeout

	@property
	def session(self):
		if not self._session:
			self._session = requests_cache.core.CachedSession(cache_name='coinmarketcap_cache', backend='sqlite', expire_after=120)
			self._session.headers.update({'Content-Type': 'application/json'})
			self._session.headers.update(
				{'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'})
		return self._session

	@retry(stop_max_attempt_number=7)
	def __request(self, endpoint, params):
		try:
			response_object = self.session.get(self.base_url + endpoint, params = params, timeout = self.request_timeout)

			if response_object.status_code != 200:
				raise Exception('An error occured, please try again.')
			
			response = json.loads(response_object.text)
			if isinstance(response, list):
				response = [dict(item, **{u'cached':response_object.from_cache}) for item in response]
			if isinstance(response, dict):
				response[u'cached'] = response_object.from_cache
		except requests.exceptions.ConnectionError as e:
			print('\na connection error occured, please try again.'+str(e)+'\n')
		except requests.exceptions.Timeout as e:
			print(f'\na timeout error occured, please try again.{e}\n')
		except requests.exceptions.RequestException as e:
			print('\na request error occured, please try again.\n')

		return response

	def ticker(self, currency="", **kwargs):
		"""
        Returns a dict containing one/all the currencies
        Optional parameters:
		(int) limit - only returns the top limit results.
		(string) convert - return price, 24h volume, and market cap in terms of another currency. Valid values are:
		"AUD", "BRL", "CAD", "CHF", "CNY", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "KRW", "MXN", "RUB"
        """

		params = {}
		params.update(kwargs)
		response = self.__request('ticker/' + currency, params)
		return response

	def stats(self, **kwargs):
		"""
		Returns a dict containing cryptocurrency statistics.
		Optional parameters:
		(string) convert - return 24h volume, and market cap in terms of another currency. Valid values are:
		"AUD", "BRL", "CAD", "CHF", "CNY", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "KRW", "MXN", "RUB"
		"""

		params = {}
		params.update(kwargs)
		response = self.__request('global/', params)
		return response

if __name__ == "__main__":
	coinmarketcap = Market()
	# for i in range (10):
	pprint(coinmarketcap.ticker("", limit=1, convert='EUR'))
		# pprint(coinmarketcap.stats())
		# pprint(coinmarketcap.ticker('', limit=3, convert='USD'))
