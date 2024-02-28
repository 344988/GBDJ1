from django.urls import path
from . import views
from .views import article_view
from .views import customer_orders_view
from .views import ordered_products_view
from .views import add_product
from .views import product_list
from django.urls import include

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('article/<int:article_id>/', article_view, name='article_view'),
    path('customer/<int:customer_id>/orders/', customer_orders_view, name='customer_orders'),
    path('customer/<int:customer_id>/ordered-products/<int:days>/', ordered_products_view, name='ordered_products'),
    path('add-product/', add_product, name='add-product'),
    path('products/', product_list, name='product-list'),
]

import debug_toolbar
urlpatterns = [
    #path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns