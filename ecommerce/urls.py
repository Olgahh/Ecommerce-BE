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
    path('categories/', views.CategoryList.as_view(), name="category-list"),
    path('categories/<int:category_id>/', views.ProductList.as_view(), name="product-list"),
    path('products/',views.AllProductList.as_view(), name="products-list"),
    #Order
    path('order/create/', views.CreateOrder.as_view(), name='create-order'),
    path('orders/', views.OrderList.as_view(), name='orders'),
    #Profile
    path("profile/",views.ProfileView.as_view(), name="profile"),
    #Authentication
    path('register/', views.RegisterView.as_view(),name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

