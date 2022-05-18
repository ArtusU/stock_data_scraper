web: gunicorn stock_scraper.wsgi --log-file -
worker: celery -A stock_scraper --beat -S django -l info