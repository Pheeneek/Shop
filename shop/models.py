from django.db import models
from django.contrib.auth.models import User as UserAuth

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    auth_user = models.OneToOneField(UserAuth, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Product(models.Model):
    PRODUCT_TYPE = (
        ('fruits', 'fruits'),
        ('vegetables', 'vegetables'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE, null=True)
    price = models.FloatField()
    discount_price = models.IntegerField()
    discount = models.IntegerField()

    def __str__(self):
        return f"{self.name}, ({self.type})"


class Coupon(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    value = models.IntegerField()
    min_coast = models.IntegerField()
    start_at = models.DateField(auto_now_add=True)
    finish_at = models.DateField()


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = (('user', 'product'), )

    def __str__(self):
        return f"{self.user}: {self.product} - {self.count} шт."


class Checkout(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = (('user', 'product'),)


class Wishlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'product'),)

    def __str__(self):
        return f"{self.user}: {self.product}"


