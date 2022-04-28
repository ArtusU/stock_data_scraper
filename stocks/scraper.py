import json
import random
import requests
from requests_html import HTML


SERVICES = {
    "business_insider": "https://markets.businessinsider.com/stocks/{ticker}-stock",
    "google_finance": "https://www.google.com/finance/quote/{ticker}:NASDAQ",
    "echo": "https://www.httpbin.org/anything/{ticker}",
}


class StockTickerScraper:
    '''
    Usage:
    StockTickerScraper(service='echo', ticker='AAPL').scrape()
    '''
    service = 'echo'
    url =  None
    ticker = 'AAPL'
    
    def __init__(self, service='echo', ticker='AAPL'):
        self.service = service
        self.url = SERVICES[service]
        self.ticker = ticker
        
    
    def scrape_echo(self, url=None):
        if url == None:
            return "", 0
        random_price = "%.2f" % (random.randint(0, 12000) / 100.00)
        r = requests.post(url, json={'ticker': self.ticker, "price": random_price})
        data = json.loads(r.json()['data'])
        return data.get('ticker'), data.get('price')
        
    
    def scrape(self, ticker=None):
        to_scrape_ticker = ticker or self.ticker
        if to_scrape_ticker == None:
            to_scrape_ticker = "AAPL"
        url = self.url.format(ticker=to_scrape_ticker)
        func = getattr(self, f"scrape_{self.service}")
        name, price = func(url)
        return name, price
        