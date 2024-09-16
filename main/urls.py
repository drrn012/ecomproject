from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_product, name='add-product'),
    path('products/json/', views.product_json, name='product-json'),
    path('products/xml/', views.product_xml, name='product-xml'),
    path('products/json/<int:id>/', views.product_json_by_id, name='product-json-by-id'),
    path('products/xml/<int:id>/', views.product_xml_by_id, name='product-xml-by-id'),
]
