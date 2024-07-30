from django.apps import AppConfig
from django_cron import CronJobManager

class BooksConfig(AppConfig):
    name = 'books'

    def ready(self):
        from .cron import DailyLikedBooksEmailJob
       