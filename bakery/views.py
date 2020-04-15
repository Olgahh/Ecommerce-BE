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
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class ProductList(ListAPIView):
    serializer_class = ProductListSerializer
    def get(self, request, category_id):
        products = Product.objects.filter(category=Category.objects.get(id=category_id))
        product_list = ProductListSerializer(products, many=True,context={"request":request}).data
        return Response(product_list, status=HTTP_200_OK)

class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

class ProfileUpdate(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'