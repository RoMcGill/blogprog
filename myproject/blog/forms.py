# forms.py

from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogCreation

class BlogPostForm(forms.Form):
    blog_name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())

class BlogPostEditForm(forms.ModelForm):
    class Meta:
        model = BlogCreation
        fields = ['blog_name', 'title', 'content']



