# forms.py

from django import forms

class BlogPostForm(forms.Form):
    blog_name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

