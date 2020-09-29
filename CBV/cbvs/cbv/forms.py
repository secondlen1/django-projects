from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=512, widget=forms.Textarea(attrs={'col':10, 'rows':20}))
    
    class Meta:
        model = Post
        fields = ['title', 'content']