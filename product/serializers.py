from rest_framework import serializers
from product.models import HomeCategory,Banner,Category,Product

class HomeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeCategory
        fields = ('typeId', 'typeName')

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('typeId', 'imageUrl', 'path', 'description')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('index', 'categoryId', 'categoryName')

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('imageUrl', 'productType', 'productTitle', 'productPrice', 'discountPrice', 'salesCount', 'couponCount', 'commission')
