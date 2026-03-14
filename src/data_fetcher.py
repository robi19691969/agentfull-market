import requests
import json

class DataFetcher:
    def __init__(self):
        self.alpha_vantage_api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
        self.iex_cloud_api_key = 'YOUR_IEX_CLOUD_API_KEY'
        self.yahoo_finance_api_key = 'YOUR_YAHOO_FINANCE_API_KEY'
        self.coingecko_base_url = 'https://api.coingecko.com/api/v3/'
        self.binance_base_url = 'https://api.binance.com/api/v3/'

    def fetch_stock_data_alpha_vantage(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={self.alpha_vantage_api_key}'
        response = requests.get(url)
        return response.json()

    def fetch_stock_data_iex_cloud(self, symbol):
        url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={self.iex_cloud_api_key}'
        response = requests.get(url)
        return response.json()

    def fetch_stock_data_yahoo_finance(self, symbol):
        url = f'https://yahoo-finance15.p.rapidapi.com/api/yahoo/finance/v1/quote?symbol={symbol}'
        headers = {
            'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com',
            'x-rapidapi-key': self.yahoo_finance_api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def fetch_crypto_data_coingecko(self, id):
        url = f'{self.coingecko_base_url}coins/markets?vs_currency=usd&ids={id}'
        response = requests.get(url)
        return response.json()

    def fetch_crypto_data_binance(self, symbol):
        url = f'{self.binance_base_url}ticker/24hr?symbol={symbol}'
        response = requests.get(url)
        return response.json()