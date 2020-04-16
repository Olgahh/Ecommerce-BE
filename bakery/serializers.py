from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category,Product,Profile

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

class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','dob','mobile','address']

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['dob','mobile','address']



