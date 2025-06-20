from django.contrib import admin

# Register your models here.
from .models import UsersModel

admin.site.register(UsersModel)