from django.db import models

from products.models import ProdutsModel, SizesModel, ColorsModel
from users.models import UsersModel

class CartModel(models.Model):
    product = models.ForeignKey(ProdutsModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    size = models.ForeignKey(SizesModel, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(ColorsModel, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    

class OrdersModel(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    payment_type = models.CharField(choices=[('1', 'Наложеный платёж'), ('2', 'Безналичный')])
    delivery_type = models.CharField(choices=[('1', 'Самовывоз'), ('2', 'Новая почта')])
    delivery_price = models.PositiveIntegerField()
    payment = models.PositiveIntegerField()
    products = models.ManyToManyField(CartModel)
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)