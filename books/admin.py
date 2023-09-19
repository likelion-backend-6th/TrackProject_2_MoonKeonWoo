from django.contrib import admin

from books.models import Book, Rental, Review


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'book_id', 'rental_date', 'return_date']
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'user_id', 'rating', 'description']