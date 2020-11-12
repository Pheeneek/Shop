from django.contrib import admin
from .models import User, Product, Cart, Coupon, Wishlist, Checkout

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Coupon)
admin.site.register(Wishlist)
admin.site.register(Checkout)
