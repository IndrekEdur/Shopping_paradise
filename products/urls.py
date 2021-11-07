"""shopping_paradise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ProductListView, my_form

urlpatterns = [


 path('list/', views.ProductListView.as_view(), name='product_list'),
 path('create/', views.ProductCreateView.as_view(), name='product_create'),
 path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
 path('update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
 path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),

 path('my-form/', my_form, name='my_form'),

 path('category_list/', views.CategoryListView.as_view(), name='category_list'),
 path('category_create/', views.CategoryCreateView.as_view(), name='category_create'),
 path('category_detail/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
 path('category_update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
 path('category_delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),
]