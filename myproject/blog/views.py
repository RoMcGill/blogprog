from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import BlogPostForm
from django.db import models
from .models import BlogCreation
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogPostEditForm



def home(request):
    return render(request, 'blog/home.html')

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
            new_blog_post = BlogCreation(  # Corrected
            blog_name=form.cleaned_data['blog_name'],
            title=form.cleaned_data['title'],
            content=form.cleaned_data['content'],
            author=request.user
            # Add additional fields as needed
        )
            new_blog_post.save()
            return render(request, 'blog/base.html')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog.html', {'form': form})


def blog_content(request):
    posts = BlogCreation.objects.all()
    context = {'posts': posts}

    if not posts.exists():  # Check if there are any posts before rendering
        context['empty_message'] = "No blog posts found!"  # Set a context variable for an empty list message (optional)

    return render(request, 'blog/blog_content.html', context)



@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogCreation, id=post_id)

    # Check if the current user is the author of the post
    if request.user != post.author:
        # Handle unauthorized access (e.g., redirect to homepage or show error message)
        return redirect('homepage')

    if request.method == 'POST':
        form = BlogPostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog/blog_content.html')
    else:
        form = BlogPostEditForm(instance=post)

    return render(request, 'blog/edit_blog_post.html', {'form': form})