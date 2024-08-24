from django.urls import path

from . import views


urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("cart/delete/<int:fk>", views.delete_cart_item, name="delete_cart"),
    path("order/", views.place_order, name="place_order"),
]
