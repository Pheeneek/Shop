from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from shop.models import User, Product, Coupon, Cart, Checkout, Wishlist
from rest_framework import mixins
from .serializer import UserSerializer, ProductSerializer, CouponSerializer, CartSerializer, CheckoutSerializer, \
    WishlistSerializer


# Create your views here.


class WishlistViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin):

    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def retrieve(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.filter(user=kwargs['pk']), many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def add(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        user = User.objects.get(pk=request.GET['user'])

        queryset = self.get_queryset()

        serializer = self.get_serializer(data=dict(user=user.pk, product=product.pk))
        serializer.is_valid(raise_exception=True)

        queryset.create(product=product, user=user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        filter_params = {param: request.GET[param] for param in request.GET}

        queryset = self.get_queryset()
        filter_queryset = queryset.filter(**filter_params)

        serializer = self.get_serializer(filter_queryset, many=True)

        return Response(serializer.data)


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CartViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.filter(user=kwargs['pk']), many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def add(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        user = User.objects.get(pk=request.GET['user'])
        count = request.GET['count']

        queryset = self.get_queryset()

        serializer = self.get_serializer(data=dict(user=user.pk, product=product.pk, count=count))
        serializer.is_valid(raise_exception=True)

        queryset.create(product=product, user=user, count=count)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CheckoutViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.filter(user=kwargs['pk']), many=True)

        return Response(serializer.data)
