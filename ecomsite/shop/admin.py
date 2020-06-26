from django.contrib import admin
from .models import Product, Order
# Register your models here.

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "Shopping portal"
admin.site.index_title = "Manage shopping portal"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category', 'description',)
    search_fields = ('title',)
    list_editable = ('price', 'category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)