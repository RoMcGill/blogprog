# forms.py

from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogCreation

class BlogPostForm(forms.Form):

    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())

class BlogPostEditForm(forms.ModelForm):
    class Meta:
        model = BlogCreation
        fields = [ 'title', 'content']



