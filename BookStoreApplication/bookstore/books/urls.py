from django.urls import path, include
from . import views

urlpatterns = [
    #route for home page
    path('', views.homepage, name='homepage'),
    #route for individual book detail
    path('book/<str:pk>/', views.book_detail, name="bookdetail"), #<int:id> allows to capture this part of URL as a variable
    #route for add book form
    path('add_book', views.add_book, name="add_book"), 
    #route for updating book
    path('book_update/<str:pk>/', views.update_book, name='update_book'),
    #route for deleting a book
    path('book_delete/<str:pk>/', views.delete_book, name='delete_book'),
    #route for registering
    path('register/',views.register , name="register"),
    #route for loging-in
    path('login_account/',views.login_account , name="login_account"),
    #route for logout
    path('logout_account/',views.logout_account, name="logout_account"),
    
]