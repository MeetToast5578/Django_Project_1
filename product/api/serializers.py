from rest_framework import serializers
from product.models import ProductCategory, Product, ProductTag
from core.models import Subscribe



class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = [
            'email'
        ]





class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductTag
        fields = [
            'id',
            'title'
        ]





class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'parent',
            'title'
        ]



class ProductSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.title')
    category = ProductCategorySerializer()
    tags = ProductTagSerializer(many= True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'description',
            'cover_image',
            'slug',
            'category',
            'tags'
        ]
        
        
        
class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'description',
            'cover_image',
            'slug',
            'category',
            'tags'
        ]