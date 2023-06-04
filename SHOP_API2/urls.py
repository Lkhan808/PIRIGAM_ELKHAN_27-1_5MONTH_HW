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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', product_list_create_api_view),
    path('api/products/reviews/', products_reviews_api_view),
    path('api/products/<int:id>/', product_retrieve_api_view),
    path('api/categories/', category_list_api_view),
    path('api/categories/<int:id>/', category_retrieve_api_view),
    path('api/reviews/', review_list_api_view),
    path('api/reviews/<int:id>/', review_retrieve_api_view),
    path('api/users', include('users.urls')),
    path('', first_view)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
