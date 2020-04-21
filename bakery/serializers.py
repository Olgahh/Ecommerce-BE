from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category,Product,OrderProduct,Order
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
############################################################################
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self, validated_data):
        new_user = User(**validated_data) #unwraps the dictionary.
        new_user.set_password(validated_data.get("password"))
        new_user.save()
        return validated_data

###########################################################################

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','image']

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'description','image','price','category']

###########################################################################

class ProductSerializer(serializers.ModelSerializer):
    product = ProductListSerializer() 
    class Meta:
        model = OrderProduct
        fields = ['product', 'order', 'quantity', 'quantity_price', 'id']

class OrderListSerializer(serializers.ModelSerializer):
    orders = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['orders', 'date_time', 'id']




###########################################################################

class ProductCreateSerializer(serializers.ModelSerializer):
      class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class OrderProductSerializer(serializers.ModelSerializer):
    orders = ProductCreateSerializer(many=True)
    class Meta:
        model = Order
        fields = ['orders']

    def create(self, validated_data):
        orders = validated_data.pop('orders')
        order = Order.objects.create(**validated_data)
        for ordr in orders:
            Product.objects.create(order=order, **ordr)
        return order