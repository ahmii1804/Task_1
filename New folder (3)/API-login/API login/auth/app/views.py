from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserProfileForm, BlogPostForm
from .models import CustomUser, BlogPost

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(user.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

@login_required
def blog_view(request):
    return render(request, 'blog.html')

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return JsonResponse({'success': True, 'blog_post': blog_post.id})
    return JsonResponse({'success': False})

@login_required
def blog_read(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    return JsonResponse({'title': blog_post.title, 'content': blog_post.content, 'author': blog_post.author.username})

@login_required
def blog_update(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def blog_delete(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    blog_post.delete()
    return JsonResponse({'success': True})