from django.urls import path
from . import views
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/rent/', views.rent_book, name='rent_book'),
    path('my_rentals/', views.RentalListView.as_view(), name='rental_list'),
]