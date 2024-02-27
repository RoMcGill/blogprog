from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('logout/', views.logout_view, name='logout'),
    path('blog-content/', views.blog_content, name='blog_content'),
    

]
