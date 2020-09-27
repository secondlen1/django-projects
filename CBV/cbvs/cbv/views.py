from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView
from .forms import PostForm
from .models import Post
# Create your views here.

class PostView(FormView):
    form_class = PostForm
    initial = {
        'title': 'Title',
        'content': 'Type your message here'
    }
    template_name = 'index.html'
    success_url = 'admin'

    def form_valid(self, form):
        form = form.cleaned_data
        Post.objects.create(title=form.get('title'), content=form.get('content'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            Post.objects.get(pk=1)
            last_post = Post.objects.all()
            last_post = last_post.order_by('-pk')[0]
            context['last_post'] = last_post
        except Post.DoesNotExist:
            context['last_post'] = False
        return context
