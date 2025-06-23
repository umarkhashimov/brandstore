from django.db import models
from users.models import UsersModel
from products.models import ProdutsModel

# Create your models here.


class CommentsModel(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(ProdutsModel, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product}"