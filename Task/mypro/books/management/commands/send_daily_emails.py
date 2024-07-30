from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User
from books.models import Book

class Command(BaseCommand):
    help = 'Send daily email with liked books'

    def handle(self, *args, **options):
        for user in User.objects.all():
            liked_books = user.liked_books.all()
            if liked_books.exists():
                books_list = '\n'.join([book.title for book in liked_books])
                send_mail(
                    'Your Liked Books',
                    f'Here are the books you liked:\n\n{books_list}',
                    'ahmiisaab18@gmail.com',
                    [user.email],
                    fail_silently=False,
                )