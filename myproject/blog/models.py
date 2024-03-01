from django.db import models
from django.contrib.auth.models import User


class BlogCreation(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()  # Use TextField for longer text content
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # Add any additional fields as needed

    def __str__(self):
        return self.title  # Customize the string representation of the model

