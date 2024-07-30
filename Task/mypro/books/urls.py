from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_signin, name='signin'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('books/', views.book_list, name='book_list'),
    path('like_book/<int:book_id>/', views.like_book, name='like_book'),
]
