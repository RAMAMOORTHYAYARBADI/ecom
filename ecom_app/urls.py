from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ManageProduct.as_view({'get':'get_all_product'})),
]