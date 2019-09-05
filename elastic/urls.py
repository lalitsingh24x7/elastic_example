from django.urls import path

from elastic.views import ProductView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products')
]
