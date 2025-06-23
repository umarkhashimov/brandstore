from django.urls import path

from .views import mainpage_view, category_view, detail_view, cart_view, write_comment_view

app_name = 'main'

urlpatterns = [
    path('', mainpage_view, name='home'),
    path('category/<int:id>', category_view, name='category'),
    path('detail/<int:id>', detail_view, name='detail'),
    path('cart/', cart_view, name='cart'),
    path('new-comment/<int:id>', write_comment_view, name='write_comment')
]
