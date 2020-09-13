from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView,LogoutView,FormView
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import Data,Img
from .polinoms import *

from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request,user)
            return redirect('login')
        
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@csrf_protect
@login_required
def home(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            Data.objects.create(user=request.user, data=request.FILES['file'])
            return redirect('show')
    else:
        form = FileForm()
    return render(request, 'home.html', {'form': form})


@csrf_protect
@login_required
def show(request):
    secondform = None
    i = None
    p = None
    polynomn = False
    try:
        d = np.genfromtxt(Data.objects.filter(user=request.user).order_by('-pk')[0].data\
            , delimiter=",", names=["x", "y"])
        x = d['x'][1:]
        y = d['y'][1:]
    except Data.DoesNotExist:
        return redirect('home')
    initials = {
        'xlim_l': min(x) - 1,
        'xlim_r': max(x) + 1,
        'ylim_l': min(y) - 1,
        'ylim_r': max(y) + 1
        }
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['choice'] == '3': # 3 is third choice = Polynom
                secondform = MNKForm(request.POST)
                polynomn = True
            else:
                secondform = GraphicForm(request.POST)
            if secondform.is_valid():
                data = secondform.cleaned_data
                k = data.get('k', None)
                lims = [data['xlim_l'], data['xlim_r'],data['ylim_l'], data['ylim_r']]
                p, i = create_img(x,y, name=str(form.cleaned_data['choice']) + str(request.user),\
                    request=request, lims=lims, k=k, title=form.cleaned_data['choice'])

            else:
                secondform = MNKForm(initial=initials) if polynomn else GraphicForm(initial=initials)

    else:
        form = ChoiceForm()
    return render(request, 'show.html', {'form': form, 'secondform': secondform, 'i': i, 'p': p})

@login_required
def profile(request):
    return render(request, 'profile.html', {'images': Img.objects.filter(user=request.user)})

    


