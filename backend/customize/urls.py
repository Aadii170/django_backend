from django.urls import path
from . import views


urlpatterns = [
    path("", views.customize, name="customize"),
    path("checkout/", views.custom_order_checkout, name="custom_order_checkout"),
]
