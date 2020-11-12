from django.urls import path
from .views import IndexView, ShopView, WishListView, \
    SingleProductView, BlogView, SingleBlogView, AboutView, ContactView, CartView, CheckView


urlpatterns = [path('', IndexView.as_view()),
               path('index/', IndexView.as_view(), name='index'),
               path('shop/', ShopView.as_view(), name='shop'),
               path('shop/<int:page>', ShopView.as_view()),
               path('wishlist/', WishListView.as_view(), name='wishlist'),
               path('single/', SingleProductView.as_view(), name='single'),
               path('blog/', BlogView.as_view(), name='blog'),
               path('blog_single/', SingleBlogView.as_view(), name='blog_single'),
               path('about/', AboutView.as_view(), name='about'),
               path('contact/', ContactView.as_view(), name='contact'),
               path('cart/', CartView.as_view(), name='cart'),
               path('checkout/', CheckView.as_view(), name='check'),
               ]
