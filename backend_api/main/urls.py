from django.urls import path,include
from main import views
from rest_framework import routers


router=routers.DefaultRouter()
router.register('address',views.CustomerAddressViewSet)
router.register('productrating',views.ProductRaitngViewSet)


urlpatterns = [
 path('api-auth',include('rest_framework.urls')),
    #vendor api
    path('vendors/',views.VendorList.as_view()),
    path('vendor/<int:pk>',views.VendorDetails.as_view()),

    # Product api
    path('products/',views.ProductList.as_view()),
    path('product/<int:pk>',views.ProductDetail.as_view()),
    # path('api/product/<int:product_id>/', views.ProductDetail.as_view(), name='product-detail'),
    path('related-products/<int:pk>',views.RelatedProductList.as_view()),

    # path('product/<slug:slug>/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),

    #category api
    path('categories/',views.CategoryList.as_view()),
    path('categories/<int:pk>',views.CategoryDetails.as_view()),

    #Customer
    path('customers/',views.CustomerList.as_view()),
    path('customer/<int:pk>',views.CustomerDetails.as_view()),
     
    #login
    path('customer/login',views.customer_login,name='customer_login'),
    path('customer/register',views.customer_register,name='customer_register'),



    #order api
    path('orders/',views.OrderList.as_view()),
    path('order/<int:pk>',views.OrderDetails.as_view()),



]

urlpatterns+=router.urls
