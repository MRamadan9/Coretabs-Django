from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug>', views.product_list_by_category, name='product_list_by_category'),
    path('products/<slug>', views.product_detail, name='product_detail'),
]