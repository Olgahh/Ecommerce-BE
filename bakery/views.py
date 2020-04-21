from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,ListAPIView,
    RetrieveAPIView,RetrieveUpdateAPIView)
from .models import *
from .serializers import( 
    RegisterSerializer,CategoryListSerializer,
    ProductListSerializer,
    OrderListSerializer,
  )
from rest_framework.permissions import (IsAuthenticated)
from .permissions import IsStaffOrOwner
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
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

class CreateOrder(APIView):
    permission_classes = [IsAuthenticated, IsStaffOrOwner]
    def post(self,request,*args,**kwargs):
        cart=request.data
        order_obj = Order.objects.create()
        for item in cart:
            product_obj = Product.objects.get(id=item.get('id'))
            quantity = item.get('quantity')
            quantity_price = item.get('quantity_price')
            orders = OrderProduct.objects.create(order=order_obj, product=product_obj, quantity=quantity,quantity_price=quantity_price)
        return Response(status=HTTP_201_CREATED)

class OrderList(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwner]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


