from django.urls import path
from .views import *

urlpatterns = [
    path('users/',custom_user_list, name='custom_user_list'),
    path('users/<int:pk>/',custom_user_detail, name='custom_user_detail'),
    path('categories/',category_list, name='category_list'),
    path('categories/<int:pk>/',category_detail, name='category_detail'),
    path('products/',product_list, name='product_list'),
    path('products/<int:pk>/',product_detail, name='product_detail'),
    path('orders/',order_list, name='order_list'),
    path('orders/<int:pk>/',order_detail, name='order_detail'),
]
