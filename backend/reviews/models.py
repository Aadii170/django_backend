from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from store.models import Products

# Create your models here.


class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review_title = models.CharField(max_length=100)
    review_text = models.CharField(max_length=500)
    rating = models.PositiveIntegerField(
        choices=(
            (1, "1 Star"),
            (2, "2 Star"),
            (3, "3 Star"),
            (4, "4 Star"),
            (5, "5 Star"),
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return self.review_title
