from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import BookSerializer
from ..models import Book

#View for book list api
@api_view(['GET'])
def get_books(request):
    "Return a list of all books."
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

#View for book detail api
@api_view(['GET'])
def get_book_detail(request, pk):
    "Return a single book by ID."
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

#View for api routes
@api_view(['GET'])
def get_api_routes(request):
    "Return a list of all available API routes."
    routes = [
        {'Books': request.build_absolute_uri("/api/books/")},
        {'Book detail': "http://127.0.0.1:8000/api/books/<ID>   **Replace ID with book id**"},
        {'Home Page': request.build_absolute_uri("/")}
    ]
    return Response(routes)
