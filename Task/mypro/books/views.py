from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.utils.timezone import now
from django.views import View


def user_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': '/books/'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password'})
    return render(request, 'books/signin.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
        
    return render(request, 'books/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'books/login.html', {'error': 'Invalid username or password'})
    return render(request, 'books/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def book_list(request):
    author_name = request.GET.get('author', '')
    if author_name:
        books = Book.objects.filter(author__name__icontains=author_name)
    else:
        books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books, 'author_name': author_name})


@login_required
def like_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.user in book.likes.all():
        book.likes.remove(request.user)
        liked = False
    else:
        book.likes.add(request.user)
        liked = True

    return JsonResponse({'liked': liked, 'total_likes': book.likes.count()})

  




