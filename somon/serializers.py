from rest_framework import serializers
from .models import CustomUser, Category, Product, Order

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer() 

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()  
    custom_id = CustomUserSerializer()  

    class Meta:
        model = Order
        fields = '__all__'
