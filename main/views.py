from django.shortcuts import render
import random
# Create your views here.

from products.models import ProdutsModel

def mainpage_view(request):

    return render(request, 'main.html')

def category_view(request):

    return render(request, 'category.html')


def detail_view(request, id):
    product = ProdutsModel.objects.get(id=id)

    recomendations = list(ProdutsModel.objects.filter(tags__in=product.tags.all()).exclude(id=product.id).distinct())

    random.shuffle(recomendations)

    context = {
        'product': product,
        'recomendations': recomendations[:4]
    }
    return render(request, 'detail.html', context)


def cart_view(request):
    return render(request, 'mycart.html')

def profile_view(request):

    return render(request, 'profile.html')

def login_view(request):
    return render(request, 'auth/login.html')