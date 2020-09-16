from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from .models import Post

# Create your views here.


@csrf_protect
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.is_superuser = True
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request,user)
            return redirect('login')
        
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    page = int(request.GET.get('page', '1'))
    tags = request.GET.get('tag', 0)
    if page < 1:
        if not request.GET._mutable:
            request.GET._mutable = True
        request.GET['page'] = '1'
        page = 1
    posts = Post.objects.all() if not tags else Post.objects.filter(tags__title=tags)
    posts = posts.order_by('-pk')
    pages = posts.count()//10
    ten_posts = posts[(page - 1)*10:(page*10)]
    return render(request,'home.html',context={
        'pages': pages,
        'posts': ten_posts,
        'page': page,
        'tag': tags
    })

def singleview(request):
    post_title = request.GET.get('title')
    post = Post.objects.get(title=post_title)
    tags = [model_to_dict(tag) for tag in model_to_dict(post)['tags']]
    return render(request, 'singleview.html',context={
        'post': post,
        'tags': tags
    })


