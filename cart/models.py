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
    