# Register your models here.
from django.contrib import admin
from .models import BlogCreation

class BlogPostAdmin(admin.ModelAdmin):
    # Specify the fields you want to display in the list view
    list_display = ('title', 'blog_name')  # Example list display

    # Optionally, customize the edit form
    fields = ('title', 'content')  # Example fields for the edit form

admin.site.register(BlogCreation, BlogPostAdmin)
