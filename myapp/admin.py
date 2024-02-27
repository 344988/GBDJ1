from django.contrib import admin

from .models import Article, Comment
from .models import Client, Product

admin.site.register(Article)
admin.site.register(Comment)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')

admin.site.register(Client, ClientAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'quantity', 'date_ordered')
    search_fields = ('client__name', 'product__name')
    list_filter = ('date_ordered',)