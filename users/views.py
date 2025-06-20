from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import RegistrationForm
from products.models import ProdutsModel
from django.shortcuts import get_object_or_404

def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('main:home')
        
    return render(request, 'auth/login.html')


def registration_view(request):

    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users:login')
        
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    context = {
        'liked': ProdutsModel.objects.filter(id__in=request.user.liked.all())
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('users:login')


def like_product_view(request, id):
    product = get_object_or_404(ProdutsModel, id=id)
    next_url = request.GET.get('next')

    if not request.user.is_authenticated:
        return redirect(next_url)

    if request.user.liked.filter(id=product.id).exists():
        request.user.liked.remove(product) 
    else:
        request.user.liked.add(product) 

    return redirect(next_url)