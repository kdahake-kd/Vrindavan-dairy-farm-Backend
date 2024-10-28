from django.db import models
from django.contrib.auth.models import User

#seller models
class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)
    
    def __str__(self):
        return self.user.username

#product category
    
class ProductCategory(models.Model):
    title=models.CharField(max_length=255)
    detail=models.TextField(null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name='product_category')
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True,null=True)  # Add this line
    detail=models.TextField(null=True)
    price=models.FloatField()
  
    image=models.ImageField(upload_to='product_imgs/',null=True)
    def __str__(self):
        return self.title
    
    

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile_no=models.PositiveBigIntegerField(unique=True,null=True)

    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer.user.username

class OrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
    


class CustomerAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_addresses')
    address=models.TextField()
    default_address=models.BooleanField(default=False)

    def __str__(self):
        return self.address



class ProductRating(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='rating_customers')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_rating')
    rating=models.IntegerField()
    reviews=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}-{self.reviews}'
    

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_imgs')
    image=models.ImageField(upload_to='product_imgs/',null=True)

    def __str__(self):
        return self.image.url
    



