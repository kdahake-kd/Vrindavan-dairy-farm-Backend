from django.contrib import admin
from .models import *
admin.site.register(Vendor)
# admin.site.register(Product)


class CustomerAdmin(admin.ModelAdmin):
    list_display=['get_username','mobile']
    def get_username(self,obj):
        return obj.user.username


admin.site.register(ProductCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(CustomerAddress)
admin.site.register(ProductRating)
admin.site.register(ProductImage)

class ProductImagesInline(admin.StackedInline):
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    inlines=[
        ProductImagesInline
    ]

admin.site.register(Product,ProductAdmin)







