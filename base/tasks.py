from celery import Celery
from django.core.management import call_command

app = Celery('yourapp')
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def scrape_and_store_ranking():
    call_command('scrape_ranking')