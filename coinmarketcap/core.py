#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:13:41 2017

@author: SPWC
"""

import json
import requests
import requests_cache
from retrying import retry
import pickle
from pprint import pprint
from fake_useragent import UserAgent

ua = UserAgent()

class Market(object):
	
	_session = None
	__DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v2/'
	__HEADER = {'user-agent': ua.chrome}
	__DEFAULT_TIMEOUT = 10
	
	
	def __init__(self, base_url = __DEFAULT_BASE_URL, request_timeout = __DEFAULT_TIMEOUT):
		self.base_url = base_url
		self.request_timeout = request_timeout

	@property
	def session(self):
		if not self._session:
			self._session = requests_cache.core.CachedSession(cache_name='coinmarketcap_cache', backend='sqlite', expire_after=120)
			self._session.headers.update({'Content-Type': 'application/json'})
			self._session.headers.update(self.__HEADER)
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


	def listings(self):
		"""
		Returns .
		"""

		params = {}
		response = self.__request('listings/', params)
		return response

	
	def ticker(self, currency="", **kwargs):
		"""
        Returns a dict containing one/100 of the currencies
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

	
	def top_100_coins(self):
		eur = self.ticker("", convert='EUR')
		gbp = self.ticker("", convert='GBP')
		btc = self.ticker("", convert='BTC')
		new_list = []
		for eur_coin, gbp_coin, btc_coin in zip(list(eur['data'].values()), list(gbp['data'].values()), list(btc['data'].values())):
			btc_coin['quotes']['EUR'] = eur_coin['quotes']['EUR']
			btc_coin['quotes']['GBP'] = gbp_coin['quotes']['GBP']
			new_list.append(btc_coin)
		with open('top_100_coins.json', 'w') as fp:
			return json.dump(new_list, fp, indent=4)

	def coin(self, ticker, convert= 'USD'):
		"""
		wrap in a retry
		"""
		def retry_if_result_none(exception):
			coin_list = self.listings()
			with open('coinlist.json', 'w') as fp:
				json.dump(coin_list['data'], fp, indent=4)
			if exception is not None:
				return isinstance(exception, FileNotFoundError)
			else:
				return exception is None
		
		@retry(retry_on_exception=retry_if_result_none, retry_on_result=retry_if_result_none, stop_max_attempt_number=2)
		def get_coin_id():
			with open('coinlist.json', 'r') as fp:
				coin_list = json.load(fp)	
			for coin in coin_list:
				if any([ticker in coin.values(), ticker.upper() in coin.values()]):
					return str(coin['id'])
		
		coin_id = get_coin_id()
		response = self.ticker(currency=coin_id, convert = convert)
		return response
			

if __name__ == "__main__":
	coinmarketcap = Market()
	pprint(coinmarketcap.coin('litecoin', 'usd'))
	#coinmarketcap.top_100_coins()
