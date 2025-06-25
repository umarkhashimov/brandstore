from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
import requests
from .models import CartModel, OrdersModel
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


def order_view(request):

    if request.method == "POST":
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        cart_products = CartModel.objects.filter(user=request.user)

        price = 0
        for cart in cart_products:
            price += cart.product.price * cart.quantity

        cart_obj = OrdersModel.objects.create(**data, delivery_price=50, payment=price, user=request.user)

        for cart in cart_products:
            cart_obj.products.add(cart)

        bot_token = '7599058591:AAG6un9TXifXsRtthKmb3wvbK-wiNocY7ak'
        user_id = 7154980539
        message = f'Новый заказ! \nName: {cart_obj.full_name}\nEmail:{cart_obj.email}\nPhone:{cart_obj.phone}\nCity:{cart_obj.city}\nSection:{cart_obj.section}\nDelivery type:{cart_obj.get_delivery_type_display()}\nPayment type: {cart_obj.get_payment_type_display()}\n\nPrice:{cart_obj.payment + cart_obj.delivery_price}\n\n Продукты:'
        
        for pr in cart_obj.products.all():
            message += f"\n\nName: {pr.product.name}\nSize: {pr.size.size_name}\nColor: {pr.color.color_name}\nLink: http://127.0.0.1:8000{reverse('main:detail', kwargs={'id': pr.product.id})}\nImage: http://127.0.0.1:8000{pr.product.img.url}"

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

        context = {
            'chat_id': user_id,
            'text':message 
        }

        response = requests.post(url, data=context)

    return redirect('main:cart')