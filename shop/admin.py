from django.contrib import admin
from .models import User, Product, Cart, Coupon, Wishlist, Checkout

# Register your models here.


class SearchAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'price']


class CartAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']


admin.site.register(User)
admin.site.register(Product, SearchAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Coupon)
admin.site.register(Wishlist)
admin.site.register(Checkout)


