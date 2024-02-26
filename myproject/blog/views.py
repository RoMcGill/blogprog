from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import BlogPostForm
from django.db import models


def home(request):
    return render(request, 'blog/base.html')


def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data and save the blog post as before
            # ... your logic to save the blog post using form.cleaned_data ...
            return render(request, 'blog/add_blog_success.html')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # Use built-in authenticate function
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to desired page after successful login
            return redirect('home')  # Replace with your desired redirect
        else:
            pass
            # Handle invalid credentials (optional)
            # ... your error handling logic ...
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog_post = BlogPost(
                blog_name=form.cleaned_data['blog_name'],
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                picture=form.cleaned_data['picture'],
                # Add additional fields as needed
            )
            new_blog_post.save()
            return render(request, 'blog/add_blog_success.html')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog.html', {'form': form})


class Blogcration_view(models.Model):
    blog_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()  # Use TextField for longer text content
    picture = models.ImageField(upload_to='blog_posts/')  # Specify upload directory
    # Add any additional fields as needed

    def __str__(self):
        return self.title  # Customize the string representation of the model




