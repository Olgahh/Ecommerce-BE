from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,ListAPIView,
    RetrieveAPIView,RetrieveUpdateAPIView)
from .models import *
from .serializers import( 
    RegisterSerializer,CategoryListSerializer,
    ProductListSerializer,
    ProfileSerializer,OrderProductSerializer,OrderListSerializer,
    TokenObtainPairWithProfileSerializer)
from rest_framework.permissions import (IsAuthenticated)
from .permissions import IsStaffOrOwner
from rest_framework_simplejwt.views import TokenObtainPairView
###########################################################################################

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
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,IsStaffOrOwner]
    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class TokenObtainPairWithProfileView(TokenObtainPairView):
	serializer_class = TokenObtainPairWithProfileSerializer
 
 ###########################################################################################

class CreateOrder(APIView):
    serializer_class=OrderProductSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwner]
    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

class OrderList(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwner]
    def get_queryset(self):
        return Order.objects.all(profile__user=self.request.user)


