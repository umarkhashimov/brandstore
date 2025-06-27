from django.shortcuts import render, redirect
import random
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import CommentsModel
from cart.models import CartModel
import requests
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
        'recomendations': recomendations[:4],
        'comments': CommentsModel.objects.filter(product=product).order_by('-id')
    }
    return render(request, 'detail.html', context)


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('main:home')
    
    products = CartModel.objects.filter(user=request.user)


    payment = 0
    for cart_item in products:
        payment += cart_item.product.price * cart_item.quantity

    context = {
        'products': products,
        'payment': payment,
        
    }
    return render(request, 'mycart.html', context)


def write_comment_view(request, id):
    product = get_object_or_404(ProdutsModel, id=id)
    
    if request.user.is_authenticated:

        if request.method == 'POST':
            text = request.POST.get('comment')

            CommentsModel.objects.create(user=request.user, product=product, comment=text)


    return redirect('main:detail', id=product.id)


def search_view(request):
    q = request.GET.get('q')
    show = request.GET.get('show')
    sort = request.GET.get('sort', None)

    products = ProdutsModel.objects.all()

    if q:
        products = products.filter(name__contains=q)

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

    paginator = Paginator(products, paginate_by) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj       
    }

    return render(request, 'category.html', context)



def email_subscribe_view(request):
    email = request.GET.get('email')

    bot_token = '7599058591:AAG6un9TXifXsRtthKmb3wvbK-wiNocY7ak'
    user_id = 7154980539
    message = f'Новая подписка: \n{email}'
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    context = {
        'chat_id': user_id,
        'text':message 
    }

    response = requests.post(url, data=context)


    next_url = request.GET.get('next')

    return redirect(next_url) 


def leave_contact_view(request):
    full_name = request.POST.get('full_name') 
    email = request.POST.get('email') 
    phone = request.POST.get('phone') 
    note = request.POST.get('note') 


    bot_token = '7599058591:AAG6un9TXifXsRtthKmb3wvbK-wiNocY7ak'
    user_id = 7154980539
    message = f'Контакт: \nИмя: {full_name}\nEmail: {email}\nPhone: {phone}\nNote: {note}'
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    context = {
        'chat_id': user_id,
        'text':message 
    }

    response = requests.post(url, data=context)

    return redirect('main:home')