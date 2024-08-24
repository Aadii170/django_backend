from django.urls import path
from .views import product_review_list_create

urlpatterns = [
    path(
        "<int:product_id>/",
        product_review_list_create,
        name="product-review-list-create",
    ),
]
