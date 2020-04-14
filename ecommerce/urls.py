"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView
from bakery import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #Products and Category
    path('products/<int:category_id>/', views.ProductList.as_view(), name="product-list"),
    path('', views.CategoryList.as_view(), name="category-list"),
    # path('product/detail/<int:product_id>/',views.ProductDetail.as_view(), name="product-detail"),

    #Profile
    path("profile/<int:profile_id>/detail/",views.ProfileDetail.as_view(), name="profile-detail"),
    path("profile/<int:profile_id>/update/",views.ProfileUpdate.as_view(), name="profile-update"),
    #Authentication
    path('register/', views.RegisterView.as_view(),name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

