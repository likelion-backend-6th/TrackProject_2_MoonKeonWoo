from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    stock = models.IntegerField()
    summary = models.TextField()

    def __str__(self):
        return self.title

class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(null=True, blank=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book_id}-{self.user_id}'

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1점'),
        (2, '2점'),
        (3, '3점'),
        (4, '4점'),
        (5, '5점')
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    description = models.TextField(null=True, default='')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)