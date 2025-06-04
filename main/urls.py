from django.urls import path

from .views import mainpage_view, category_view

app_name = 'main'

urlpatterns = [
    path('', mainpage_view, name='home'),
    path('category/', category_view, name='category')
]
