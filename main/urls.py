from django.urls import path

from .views import mainpage_view

app_name = 'main'

urlpatterns = [
    path('', mainpage_view, name='home')
]
