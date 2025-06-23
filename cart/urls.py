from django.urls import path

from .views import detele_from_cart, add_to_cart

app_name = 'cart'

urlpatterns = [
    path('cart/remove/<int:id>', detele_from_cart, name='delete_cart'),
    path('cart/add/<int:id>', add_to_cart, name='add_cart')
]
