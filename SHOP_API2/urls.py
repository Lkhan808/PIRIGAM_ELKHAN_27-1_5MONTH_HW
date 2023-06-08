"""
URL configuration for SHOP_API2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from SHOP_API2 import settings
from django.conf.urls.static import static

from product.views import *


list_create = {
    'get': 'list',
    'post': 'create'}

update_retrieve_destroy = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductModelViewSet.as_view(list_create), name='ProductListView'),
    path('api/products/reviews/', ReviewProductAPIView.as_view()),
    path('api/products/<int:pk>/', ProductModelViewSet.as_view(update_retrieve_destroy), name='ProductListView'),
    path('api/categories/', CategoryModelView.as_view(list_create), name='CategoryAPIView'),
    path('api/categories/<int:pk>/', CategoryModelView.as_view(update_retrieve_destroy), name='CategoryAPIView'),
    path('api/reviews/', ReviewModelView.as_view(list_create), name='ReviewAPIView'),
    path('api/reviews/<int:pk>/', ReviewModelView.as_view(update_retrieve_destroy), name='ReviewAPIView'),
    path('api/users/', include('users.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
