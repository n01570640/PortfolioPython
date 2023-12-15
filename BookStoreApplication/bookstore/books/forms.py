#importing modelForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Book

#create movie form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        #Exclude 'posted_by' as it is not accepted by form input
        exclude = ['posted_by']

