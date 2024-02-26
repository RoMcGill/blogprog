from django.db import models

class BlogCreation(models.Model):
    blog_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()  # Use TextField for longer text content
    picture = models.ImageField(upload_to='blog_posts/')  # Specify upload directory
    # Add any additional fields as needed

    def __str__(self):
        return self.title  # Customize the string representation of the model

