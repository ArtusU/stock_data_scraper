from django.db import models



STOCK_MARKET_LOOKUP_SOURCES = (
    ('business_insider', 'Business Insider Markets'),
    ('google_finance', 'Google Finance'),
    ('echo', 'Http Bin Echo'),    
)

class Company(models.Model):
    name = models.CharField(max_length=220)
    ticker = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    scraping_scheduler_enabled = models.BooleanField(default=False)
    has_granular_scraping = models.BooleanField(default=False)
    one_off_scrape = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} ({self.ticker})"
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    
    
class PriceLookupEvent(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    ticker = models.CharField(max_length=20)
    name = models.CharField(max_length=220, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=50, choices=STOCK_MARKET_LOOKUP_SOURCES, default='echo')
    timestamp = models.DateTimeField(auto_now_add=True)
