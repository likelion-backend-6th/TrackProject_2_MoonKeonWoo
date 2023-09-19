from datetime import datetime

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from accounts.models import CustomUser
from books.models import Book, Rental, Review


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

def return_book(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    book = get_object_or_404(Book, pk=pk)
    rental.delete()
    book.stock += 1
    book.save()

    return HttpResponseRedirect('/books/my_rentals')

class RentalListView(ListView):
    model = Rental
    template_name = 'books/rental_list.html'
    context_object_name = 'rent_list'
    def get_queryset(self):
        queryset = super().get_queryset().filter(user_id=self.request.user)
        return queryset
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating', 'description', 'book_id', 'user_id']
class ReviewCreateView(CreateView):
    model = Review
    template_name = 'reviews/review_form.html'
    # form_class = ReviewForm
    fields = ['rating', 'description', 'book_id', 'user_id']
    success_url = '/'
    # try1
    # def form_valid(self, form):
    #     book = get_object_or_404(Book, pk=self.kwargs['pk'])
    #     user = get_object_or_404(CustomUser, pk=self.request.user.id)
    #
    #     # 폼 인스턴스에 user_id와 book_id 설정
    #     form.instance.user_id = user
    #     form.instance.book_id = book
    #
    #     return super().form_valid(form)
    # try2
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     book = get_object_or_404(Book, pk=self.kwargs['pk'])
    #     user = self.request.user
    #
    #     kwargs['initial'] = {
    #         'book_id': book,
    #         'user_id': user,
    #     }
    #
    #     return kwargs
    # try3
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     book = get_object_or_404(Book, pk=self.kwargs['pk'])
    #     user = self.request.user
    #
    #     context['book_id'] = book
    #     context['user_id'] = user.id
    #
    #     return context