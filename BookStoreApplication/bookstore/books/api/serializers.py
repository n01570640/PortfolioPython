from rest_framework import serializers
from ..models import Book
#create serializer for book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'