import datetime
from django.core.management.base import BaseCommand
from base.models import Player
from base.scraper import scraping ,scrapingutr 
import time
from selenium import webdriver

class Command(BaseCommand):
    help = 'Scrape player rankings and update the data attribute'
    

    def handle(self, *args, **options):
        players=Player.objects.all()
        for player in players:
            ranking_data = scraping(player.url) 
            utr=scrapingutr(player.utrurl)
            date = datetime.date.today()
            high=ranking_data[0]
            low=ranking_data[2]


    
   
        # Convert the date to a string before serializing
            date_str = date.strftime("%Y-%m-%d")
            # Update data attribute with the scraped ranking and date
            # output.append({
            #     'high': high,
            #     'low': low,
            #     'date': date_str,
            # })
            player.data.append({
                'utr':utr,
                'high': high,
                'low': low,
                'date': date_str,
            })

            player.save()
        self.stdout.write(self.style.SUCCESS('Scraping completed successfully'))