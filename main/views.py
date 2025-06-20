from django.shortcuts import render
import random
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
# Create your views here.

from products.models import ProdutsModel, TagsModel

def mainpage_view(request):
    context = {
        'catalog': ProdutsModel.objects.all().order_by('-id')[:9],
        'prints': ProdutsModel.objects.all()[:15],
    }
    return render(request, 'main.html', context)

def category_view(request, id):
    category = get_object_or_404(TagsModel, id=id)

    products = ProdutsModel.objects.filter(tags=category)

    sort = request.GET.get('sort', None)
    show = request.GET.get('show', None)

    if sort:
        if sort == '1':
            products = products.order_by('price')
        elif sort == '2':
            products = products.order_by('-price')
        elif sort == '3':
            products = products.order_by('name')

    paginate_by = 16
    if show:
        paginate_by = int(show)

    paginator = Paginator(products, paginate_by)  # 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "category" : category,
        'page_obj': page_obj       
    }
    return render(request, 'category.html', context)


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