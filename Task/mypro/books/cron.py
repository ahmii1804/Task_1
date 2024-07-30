from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from .models import Book, User

class DailyLikedBooksEmailJob(CronJobBase):
    RUN_AT_TIMES = ['00:00']  # run daily at midnight

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'books.daily_liked_books_email_job'  # a unique code

    def do(self):
        users = User.objects.all()
        for user in users:
            liked_books = Book.objects.filter(likes__user=user)
            book_list = '\n'.join([book.title for book in liked_books])
            send_mail(
                'Your Liked Books',
                f'You liked the following books:\n{book_list}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )