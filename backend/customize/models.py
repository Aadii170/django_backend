from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from store.models import Phones

# Create your models here.


class Customize(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/customize")
    name_on_cover = models.CharField(max_length=100, default=None)
    quantity = models.IntegerField(default=1)
    ammount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=10, default=None)
    phone_model = models.ForeignKey(
        Phones, on_delete=models.SET_NULL, blank=True, null=True
    )
