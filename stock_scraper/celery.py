import os

from celery import Celery
from celery.schedules import crontab

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_scraper.settings')

app = Celery('stock_scraper')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.timezone = 'Europe/London'
app.conf.broker_url = BASE_REDIS_URL
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'