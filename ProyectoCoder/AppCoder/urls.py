from django.urls import path
from AppCoder.views import create_product_form, search_product, show_html, show_products

urlpatterns = [
    path('crear-producto/', create_product_form),
    path('buscar/', search_product),
    path('show/', show_html),
    path('productos/', show_products),
]