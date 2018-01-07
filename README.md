<h1><img src="https://raw.githubusercontent.com/SPWC/coinmarketcap/master/doc/SPWC_Crypto_Bot.png" height=85 alt="coinmarketcap" title="coinmarketcap">coinmarketcap</h1>


**Please note that all results are cached for 120 seconds.**

## API Documentation:

This API can currently retrieve the following data from [coinmarketcap](http://coinmarketcap.com/):

- **`GET /v1/ticker/`**
- **`GET /v1/ticker/currency`**
- **`Optional parameters:`**
    - **(int) start** - return results from rank [start] and above
    - **(int) limit** - only returns the top limit results.
    - **(string) convert** - return price, 24h volume, and market cap in terms of another currency. Valid values are:
"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"
```python
>>> from coinmarketcap import Market
>>> coinmarketcap = Market()
>>> coinmarketcap.ticker(<currency>, limit=3, convert='EUR')
[
    {
        "market_cap_usd": "46511837774.0",
        "price_usd": "2840.01",
        "last_updated": "1496839152",
        "name": "Bitcoin",
        "24h_volume_usd": "1653540000.0",
        "percent_change_7d": "28.25",
        "symbol": "BTC",
        "rank": "1",
        "percent_change_1h": "0.17",
        "total_supply": "16377350.0",
        "price_btc": "1.0",
        "available_supply": "16377350.0",
        "market_cap_eur": "41469908047.0",
        "percent_change_24h": "-1.63",
        "24h_volume_eur": "1474294610.46",
        "id": "bitcoin",
        "price_eur": "2532.15007599"
    },
    {
        "market_cap_usd": "24216937775.0",
        "price_usd": "262.428",
        "last_updated": "1496839164",
        "name": "Ethereum",
        "24h_volume_usd": "576588000.0",
        "percent_change_7d": "13.56",
        "symbol": "ETH",
        "rank": "2",
        "percent_change_1h": "0.22",
        "total_supply": "92280312.0",
        "price_btc": "0.0932293",
        "available_supply": "92280312.0",
        "market_cap_eur": "21591797503.0",
        "percent_change_24h": "0.72",
        "24h_volume_eur": "514085284.212",
        "id": "ethereum",
        "price_eur": "233.980542372"
    },
    {
        "market_cap_usd": "10803955417.0",
        "price_usd": "0.279738",
        "last_updated": "1496839144",
        "name": "Ripple",
        "24h_volume_usd": "110956000.0",
        "percent_change_7d": "27.08",
        "symbol": "XRP",
        "rank": "3",
        "percent_change_1h": "-0.15",
        "total_supply": "99994661895.0",
        "price_btc": "0.00009938",
        "available_supply": "38621693933.0",
        "market_cap_eur": "9632795846.0",
        "percent_change_24h": "-3.87",
        "24h_volume_eur": "98928258.644",
        "id": "ripple",
        "price_eur": "0.2494141211"
    }
]
```

- **`GET /v1/global/`**
- **`Optional parameters:`**
    - **(string) convert** - return price, 24h volume, and market cap in terms of another currency. Valid values are:
"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"


```python
>>> coinmarketcap.stats()
{
    "bitcoin_percentage_of_market_cap": 45.71,
    "total_market_cap_usd": 101753095791.0,
    "active_markets": 4046,
    "active_assets": 121,
    "total_24h_volume_eur": 3199756517.0,
    "active_currencies": 745,
    "total_market_cap_eur": 90722958453.0,
    "total_24h_volume_usd": 3588784327.0
}
```
