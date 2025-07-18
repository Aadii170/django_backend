from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()
    image = models.ImageField(upload_to="images/categories/", blank=True)

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()
    # image = models.ImageField(upload_to='images/categories/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        SubCategories, on_delete=models.CASCADE, blank=True, null=True
    )
    image = models.ImageField(upload_to="images/products/", blank=True)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Phones(models.Model):
    model = models.CharField(max_length=50)
