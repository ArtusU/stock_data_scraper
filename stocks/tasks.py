import datetime
import time
from celery import shared_task
from django.apps import apps
from .scraper import StockTickerScraper


@shared_task
def hello_world(num=10):
    time.sleep(num)
    print(f"Hello world {num}")
    

@shared_task
def perform_scrape(ticker='GOOG', service='echo'):
    client = StockTickerScraper(service=service)
    name, price = client.scrape(ticker=ticker)
    PriceLookupEvent = apps.get_model("stocks", "PriceLookupEvent")
    PriceLookupEvent.objects.create_event(ticker=ticker, price=price, name=name, service=service)
    

@shared_task
def company_price_scrape_task(instance_id, service='echo'):
    Company = apps.get_model("stocks", "Company")
    obj = Company.objects.get(id=instance_id)
    ticker = obj.ticker
    perform_scrape(ticker=ticker, service=service)
    

@shared_task
def company_granular_price_scrape_task(instance_id, service='echo'):
    Company = apps.get_model("stocks", "Company")
    obj = Company.objects.get(id=instance_id)
    ticker = obj.ticker
    perform_scrape(ticker=ticker, service=service)
    if obj.has_granular_scraping:
        now = datetime.datetime.now()
        expires = now + datetime.timedelta(seconds=65)
        for i in range(1, 60): # 1 - 59
            perform_scrape.apply_async(kwargs={
                "ticker": ticker,
                "service": service
            }, countdown=i, expires=expires)