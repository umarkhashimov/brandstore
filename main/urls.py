from django.urls import path

from .views import mainpage_view, category_view, detail_view, cart_view

app_name = 'main'

urlpatterns = [
    path('', mainpage_view, name='home'),
    path('category/', category_view, name='category'),
    path('detail/', detail_view, name='detail'),
    path('cart/', cart_view, name='cart')
]
