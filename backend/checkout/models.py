import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

from store.models import Products, Phones

# from payments.models import Transaction


# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    pin_code = models.IntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(000000)]
    )
    phone_model = models.ForeignKey(
        Phones, on_delete=models.SET_NULL, blank=True, null=True
    )

    phone_no = models.BigIntegerField()
    is_custom = models.BooleanField(default=False)
    name_on_cover = models.CharField(max_length=100, blank=True, null=True, default="")
    image = models.ImageField(
        upload_to="images/customize", blank=True, null=True, default=None
    )
    items = ArrayField(models.IntegerField(), blank=True, null=True, default=None)
    total = models.FloatField()
    payment_option = models.CharField(
        max_length=50, default="ONLINE", choices=[("COD", "COD"), ("ONLINE", "ONLINE")]
    )
    placed = models.BooleanField(default=False)
