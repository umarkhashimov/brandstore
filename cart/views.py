from django.shortcuts import redirect, get_object_or_404

from .models import CartModel
from products.models import ProdutsModel, SizesModel, ColorsModel


def detele_from_cart(request, id):

    if not request.user.is_authenticated:
        return redirect('main:home')
    
    cart_obj = get_object_or_404(CartModel, id=id)

    cart_obj.delete()

    return redirect('main:cart')


def add_to_cart(request, id):
    product = get_object_or_404(ProdutsModel, id=id)
    if not request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
        size = SizesModel.objects.get(id=request.POST.get('size'))
        color = ColorsModel.objects.get(id=request.POST.get('color'))
        quantity = 1 if not request.POST.get('quantity') else request.POST.get('quantity')

        new_cart = CartModel.objects.create(user=request.user, product=product, size=size, color=color, quantity=quantity)
        

    return redirect('main:detail', id=product.id)