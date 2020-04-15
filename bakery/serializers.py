from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category,Product,Profile,Image

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username","first_name" ,"last_name","email","password"]


    def create(self, validated_data):
        new_user = User(**validated_data) #unwraps the dictionary.
        new_user.set_password(validated_data.get("password"))
        new_user.save()
        return validated_data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','image']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','name','description','images','price','category']

class ProfileDetailSerializer(serializers.ModelSerializer):
    update = serializers.HyperlinkedIdentityField(
        view_name="update",
        lookup_field="id",
        lookup_url_kwarg="profile_id"
    )
    class Meta:
        model = Profile
        fields = ['dob','mobile','update']

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['dob','mobile']

# class ProfileSerializer(serializers.ModelSerializer):
# 	name = serializers.SerializerMethodField()
# 	class Meta:
# 		model = User
# 		fields = ["username", "name", "email","mobile","date_of_birth"]
# 	def name(self, obj):
# 		return "%s %s"%(obj.first_name, obj.last_name)