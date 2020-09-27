from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=512)
    
    class Meta:
        model = Post
        fields = ['title', 'content']