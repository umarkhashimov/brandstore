from django.shortcuts import render

# Create your views here.


def mainpage_view(request):

    return render(request, 'main.html')

def category_view(request):

    return render(request, 'category.html')


def detail_view(request):
    return render(request, 'detail.html')


def cart_view(request):
    return render(request, 'mycart.html')

def profile_view(request):

    return render(request, 'profile.html')

def login_view(request):
    return render(request, 'auth/login.html')