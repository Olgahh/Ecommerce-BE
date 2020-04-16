from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,ListAPIView,
    RetrieveAPIView,RetrieveUpdateAPIView)
from .models import Category,Product, Profile
from .serializers import( 
    RegisterSerializer,CategoryListSerializer,
    ProductListSerializer,ProfileDetailSerializer,
    ProfileUpdateSerializer)
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

###########################################################################################

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]

class ProductList(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        products = Product.objects.filter(category_id=self.kwargs.get("category_id"))
        return products

class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

###########################################################################################

class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

class ProfileUpdate(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'