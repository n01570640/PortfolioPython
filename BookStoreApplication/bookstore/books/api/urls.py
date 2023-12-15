from django.urls import path
from .views import get_books, get_book_detail, get_api_routes

urlpatterns = [
    #route for books list api
    path('books/', get_books, name='api-books'),
    #route for book detail api
    path('books/<int:pk>/', get_book_detail, name='api-book-detail'),
    #route for api routes
    path('', get_api_routes, name='api-routes'),
]