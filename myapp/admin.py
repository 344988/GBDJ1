from django.contrib import admin
from .models import Article, Comment
from .models import Client, Product, Order

admin.site.register(Article)
admin.site.register(Comment)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'quantity', 'date_ordered')
    search_fields = ('client__name', 'product__name')
    list_filter = ('date_ordered',)