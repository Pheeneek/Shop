from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator, EmptyPage

from .settings.info import INFO
# Create your views here.


class CartView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, 'shop/cart.html', context)


class CheckView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, 'shop/Checkout.html', context)


class ContactView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, 'shop/contact.html', context)


class AboutView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, 'shop/about.html', context)


class IndexView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, 'shop/index.html', context)


class WishListView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, "shop/wishlist.html", context)


class SingleProductView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, "shop/product-single.html", context)


class BlogView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, "shop/blog.html", context)


class SingleBlogView(View):
    def get(self, request):
        context = {}
        context.update(INFO)
        return render(request, "shop/blog-single.html", context)


class ShopView(View):
    def get(self, request, page=1):
        products_list = [
            {
                'name': 'Bell Pepper',
                'image': 'shop/images/product-1.jpg',
                'price': '$150.00',
                'discount': '30%',
                'price_sale': '$100.00'
            },
            {
                'name': 'Strawberry',
                'image': 'shop/images/product-2.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Green Beans',
                'image': 'shop/images/product-3.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Purple Cabbage',
                'image': 'shop/images/product-4.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Tomatoe',
                'image': 'shop/images/product-5.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Brocolli',
                'image': 'shop/images/product-6.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Carrots',
                'image': 'shop/images/product-7.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Fruit Juice',
                'image': 'shop/images/product-8.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Onion',
                'image': 'shop/images/product-9.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Apple',
                'image': 'shop/images/product-10.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Garlic',
                'image': 'shop/images/product-11.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Chilli',
                'image': 'shop/images/product-12.jpg',
                'price': '$120.00'
            }
        ]

        product_on_page = 4
        paginator = Paginator(products_list, product_on_page)

        try:
            products_list = paginator.page(page)
            products_list.page_tuple = tuple(paginator.page_range)
        except EmptyPage:
            return redirect(reverse('shop'))

        contex = {'page_obj': products_list}
        contex.update(INFO)
        return render(request, 'shop/shop.html', contex)
