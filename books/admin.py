from django.contrib import admin

from books.models import Book, Rental

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'book_id', 'rental_date', 'return_date']