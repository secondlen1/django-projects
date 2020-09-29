from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, ListView, DeleteView
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
    success_url = 'list'

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


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    extra_context = {
        'latest': Post.objects.all().order_by('-pk')[:3]
    }

    template_name = 'detail.html'

class PostsList(ListView):
    context_object_name = 'posts'
    template_name = 'list.html'
    model = Post
    paginate_by = 2
    paginate_orphans = 1


class DeletePost(DeleteView):
    model = Post
    template_name = 'post_check_delete.html'
    success_url = reverse_lazy('list')


def list_view(request):
    pass