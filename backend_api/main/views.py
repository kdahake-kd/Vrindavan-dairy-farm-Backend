from django.shortcuts import render
from rest_framework import generics,permissions,pagination,viewsets
from main.models import *
from main import serializers
from main.pagination import CustomPagination
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

class VendorList(generics.ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    # permission_classes=[permissions.IsAuthenticated]

class VendorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class=serializers.VendorDetailsSerializer



# class ProductList(generics.ListCreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=serializers.ProductListSerializer
#     pagination_class = pagination.PageNumberPagination

#     def get_queryset(self):
#         qs = super().get_queryset()
#         category_id = self.request.GET.get('category_id')  # Use 'get' to avoid KeyError
#         if category_id:
#             try:
#                 category = ProductCategory.objects.get(id=category_id)
#                 qs = qs.filter(category=category)
#             except ProductCategory.DoesNotExist:
#                 pass  # Handle error if needed
#         return qs
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.GET.get('category_id')  # Use 'get' to avoid KeyError
        if category_id:
            try:
                # Get the category object if it exists
                category = ProductCategory.objects.get(id=category_id)
                # Filter the products based on the category
                qs = qs.filter(category=category)
            except ProductCategory.DoesNotExist:
                # Handle the case where the category does not exist
                qs = qs.none()  # Return an empty queryset
        return qs


class RelatedProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductListSerializer
    pagination_class=pagination.PageNumberPagination

    def get_queryset(self):
        qs=super().get_queryset()
        product_id=self.kwargs['pk']
        product=Product.objects.get(id=product_id)
        qs=qs.filter(category=product.category).exclude(id=product_id)
        return qs





class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=serializers.CustomerSerializer
    # permission_classes=[permissions.IsAuthenticated]

class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=serializers.CustomerDetailsSerializer

class OrderList(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=serializers.OrderSerializer

class OrderDetails(generics.ListAPIView):
    # queryset=OrderItems.objects.all()
    serializer_class=serializers.OrderDetailsSerializer

    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=Order.objects.get(id=order_id)
        order_items=OrderItems.objects.filter(order=order)
        return order_items     

class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset=CustomerAddress.objects.all()
    serializer_class=serializers.CustomerAddressSerializer   


class ProductRaitngViewSet(viewsets.ModelViewSet):
    queryset=ProductRating.objects.all()
    serializer_class=serializers.ProductRatingSerializer  


class CategoryList(generics.ListCreateAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class=serializers.CategorySerializer
    pagination_class = pagination.PageNumberPagination
    # permission_classes=[permissions.IsAuthenticated]

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class=serializers.CategoryDetailsSerializer

@csrf_exempt
def customer_login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    print(password)
    user=authenticate(username=username,password=password)
    print(user)
    if user:
        msg={
            'bool':True,
            'user':user.username
        }
    else:
        msg={
            'bool':False,
            'msg':"Invalid username/password!"
        }
        
    return JsonResponse(msg)



@csrf_exempt
def customer_register(request):
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    username=request.POST.get('username')
    email=request.POST.get('email')
    mobile=request.POST.get('mobile')

    password=request.POST.get('password')

    try:

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

        try:
        
            if user:

                customer=Customer.objects.create(
                    user=user,
                    mobile_no=mobile
                )
                msg={
                    'bool':True,
                    'user':user.id,
                    'customerid ':customer.id,
                    'msg':"Thank you , Your Registration is Done "

                }
            else:
                msg={
                    'bool':False,
                    'msg':"Ooops Something Went Wrong!!!"
                }
        except IntegrityError:
            msg={
                    'bool':False,
                    'msg':"Mobile Number Already Exist"
                }

    except IntegrityError:
        msg={
                'bool':False,
                'msg':"Username is alreday exits ..... try different one"
            }

        
    return JsonResponse(msg)