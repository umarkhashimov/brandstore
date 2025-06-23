from django.contrib import admin

# Register your models here.
from .models import CommentsModel

admin.site.register(CommentsModel)