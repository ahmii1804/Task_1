from django.urls import path
from .views import signup_view, login_view, profile_view, blog_view, blog_create, blog_read, blog_update, blog_delete

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('blog/', blog_view, name='blog'),
    path('api/blog/create/', blog_create, name='blog_create'),
    path('api/blog/read/<int:id>/', blog_read, name='blog_read'),
    path('api/blog/update/<int:id>/', blog_update, name='blog_update'),
    path('api/blog/delete/<int:id>/', blog_delete, name='blog_delete'),
]