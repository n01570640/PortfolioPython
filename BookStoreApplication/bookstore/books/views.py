from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError, DatabaseError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required #for resitricting access
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Book
from .forms import BookForm
# Create your views here.
#View for home page
def homepage(request):
    books = Book.objects.all() #Fetch all books
    context = {
        "page_title": "Books",
        "books_array": books
    }
    return render(request, 'homepage.html', context)

#View for regiserting
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()#creates new user in db
            messages.success(request, 'Account created successfully')
            #Redirect to login page
            return redirect('login_account')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")

    else:
        #when user first navigates to register page
        form = UserCreationForm()
    return render(request, 'register.html', {'form' : form})

#View for loging-in
def login_account(request):
    if request.method == 'POST':
        #form for user authentication
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')#extract validated form data
            password = form.cleaned_data.get('password')#extract validated form data
            #to verify user credentials
            user = authenticate(username=username, password=password)#returns user obj or None
            if user is not None:#user found
                login(request, user)
                return redirect('/') #redirect to the home page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        #when user first navigates to login page
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

#View for logout
def logout_account(request):
    logout(request)#logout
    return redirect('login_account')

#View for individual book
def book_detail(request, pk):
    # Get a single book by id or return a 404 error if not found
    book = get_object_or_404(Book, id=pk)
    context = {
        "page_title": "Book",
        "book": book,
    }
    return render(request, 'bookdetail.html', context)

#View for adding a book using form
@login_required
def add_book(request):
    #print("Add book view called")
    error_messages = []
    #create book object from form
    form = BookForm(request.POST or None)
    #When form submitted
    if (request.method) == 'POST':
        if form.is_valid():
            try:
                new_book = form.save(commit=False)
                new_book.posted_by = request.user
                new_book.save()
                #print("Book saved successfully.")
                return redirect('/')
            except (IntegrityError, DatabaseError) as e:
                error_messages.append('A database error occurred: ' + str(e))
            except Exception as e:
                error_messages.append('An unexpected error occurred: ' + str(e))
        else:
            print("Form is invalid")
            print("Form errors:", form.errors)
            for field in form:
                for error in field.errors:
                    error_messages.append(f"{field.label}: {error}")
        
    context = {'form': form, "errors": error_messages}
    return render(request, 'book_form.html', context)

#View to update the book info
def update_book (request, pk):
    #Get book object from db with id using model
    book = get_object_or_404(Book, id=pk)
    # Check if the logged-in user is the same as the one who posted the book
    if book.posted_by != request.user:
        messages.error(request, "You do not have permission to edit this book.")
        return render(request, 'bookdetail.html', {'book': book})
    
    error_messages = []  # List to store error messages
    # When form submitted get values
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except (IntegrityError, DatabaseError) as e:
                # Handle database errors
                error_messages = ['A database error occurred: ' + str(e)]
            except Exception as e:
                # Handle any other exceptions
                error_messages = ['An unexpected error occurred: ' + str(e)]
        else:
            error_messages = [f"{field.label}: {error}" for field in form for error in field.errors]
    else:
        form = BookForm(instance=book)
        error_messages = []

    context = {'form': form, 'book': book, 'errors': error_messages, "is_update": True}
    return render(request, 'book_form.html', context)

#View to delete a book by id
def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    error_message = None
    # Check if the logged-in user is the same as the one who posted the book
    if book.posted_by != request.user:
        messages.error(request, "You do not have permission to edit this book.")
        return render(request, 'bookdetail.html', {'book': book})
    
    if request.method == 'POST':
        try:
            book.delete()
            return redirect('/')  # Redirect to the homepage on successful deletion
        except (IntegrityError, DatabaseError) as e:
            error_message = 'A database error occurred while deleting the book.'
        except Exception as e:
            error_message = 'An unexpected error occurred while deleting the book.'
    #Render confirm delete page
    return render(request, 'delete.html', {'book': book, "error_message": error_message})
