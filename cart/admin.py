from django.contrib import admin

from .models import CartModel, OrdersModel

admin.site.register(CartModel)
admin.site.register(OrdersModel)