from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from books.models import Book, Rental


# Create your views here.
class Index(ListView):
    model = Book
    template_name = 'books/index.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'

def rent_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.stock > 0:
        rental = Rental(book_id=book, user_id=request.user)
        rental.save()
        book.stock -= 1
        book.save()
    return HttpResponseRedirect('/books/my_rentals')

class RentalListView(ListView):
    model = Rental
    template_name = 'books/rental_list.html'
    context_object_name = 'rent_list'
    def get_queryset(self):
        queryset = super().get_queryset().filter(user_id=self.request.user)
        return queryset