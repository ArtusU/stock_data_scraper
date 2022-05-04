import time
from celery import shared_task
from .scraper import StockTickerScraper
from .models import PriceLookupEvent


@shared_task
def hello_world(num=10):
    time.sleep(num)
    print(f"Hello world {num}")
    

@shared_task
def perform_scrape(ticker='GOOG', service='echo'):
    client = StockTickerScraper(service=service)
    name, price = client.scrape(ticker=ticker)
    PriceLookupEvent.objects.create_event(ticker=ticker, price=price, name=name, service=service)