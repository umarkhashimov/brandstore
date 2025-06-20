from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from products.models import ProdutsModel


class UsersModel(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    liked = models.ManyToManyField(ProdutsModel)