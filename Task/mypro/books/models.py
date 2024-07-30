from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_books', blank=True)

    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title







