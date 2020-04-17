from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,ListAPIView,
    RetrieveAPIView,RetrieveUpdateAPIView)
from .models import Category,Product, Profile
from .serializers import( 
    RegisterSerializer,CategoryListSerializer,
    ProductListSerializer,
    ProfileSerializer)
from rest_framework.response import Response
# from rest_framework.permissions import (AllowAny)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

###########################################################################################

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class ProductList(ListAPIView):
    serializer_class = ProductListSerializer
    def get_queryset(self):
        products = Product.objects.filter(category_id=self.kwargs.get("category_id"))
        return products

class AllProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
  
###########################################################################################

class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'