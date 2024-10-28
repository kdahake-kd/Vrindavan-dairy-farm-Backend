from main import serializers as seri
from rest_framework import serializers
from main import models



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']

    def __init__(self, *args, **kwargs):
        super(VendorSerializer,self).__init__(*args ,**kwargs)
        # self.Meta.depth=1


class VendorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']
    def __init__(self, *args, **kwargs):
        super(VendorDetailsSerializer,self).__init__(*args ,**kwargs)
        # self.Meta.depth=1


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductImage
        fields=['id','product','image']

class ProductListSerializer(serializers.ModelSerializer):
    product_rating=serializers.StringRelatedField(many=True,read_only=True)
    # product_imgs=ProductImageSerializer(many=True,read_only=True)
    

    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','slug','detail','price','product_rating','image']
    def __init__(self, *args, **kwargs):
        super(ProductListSerializer,self).__init__(*args ,**kwargs)
        # self.Meta.depth=1


class ProductDetailSerializer(serializers.ModelSerializer):
    product_rating=serializers.StringRelatedField(many=True,read_only=True)
    product_imgs=ProductImageSerializer(many=True,read_only=True)

    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','slug','detail','price','product_rating','product_imgs']
    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer,self).__init__(*args ,**kwargs)
        # self.Meta.depth=1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile_no']

    def __init__(self, *args, **kwargs):
        super(CustomerSerializer,self).__init__(*args ,**kwargs)
        self.Meta.depth=1


class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile_no']
    def __init__(self, *args, **kwargs):
        super(CustomerDetailsSerializer,self).__init__(*args ,**kwargs)
        self.Meta.depth=1

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields=['id','customer']

    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self).__init__(*args ,**kwargs)
        self.Meta.depth=1

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.OrderItems
        fields=['id','order','product']
    def __init__(self, *args, **kwargs):
        super(OrderDetailsSerializer,self).__init__(*args ,**kwargs)
        self.Meta.depth=1


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CustomerAddress
        fields=['id','customer','address','default_address']
    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer,self).__init__(*args ,**kwargs)
        self.Meta.depth=1


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductRating
        fields=['id','customer','product','rating','reviews','add_time']
    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer,self).__init__(*args ,**kwargs)
        self.Meta.depth=1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductCategory
        fields=['id','title','detail']

    def __init__(self, *args, **kwargs):
        super(CategorySerializer,self).__init__(*args ,**kwargs)
        # self.Meta.depth=1


class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductCategory
        fields=['id','title','detail']
    def __init__(self, *args, **kwargs):
        super(CategoryDetailsSerializer,self).__init__(*args ,**kwargs)
        # self.Meta.depth=1



