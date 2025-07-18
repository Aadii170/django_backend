from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("category/<name>", views.categories, name="categories"),
    path("subcategory/<name>", views.subcategories, name="subcategories"),
    path("product/<str:pk>/", views.products, name="products"),
    # wishlist
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/delete/<str:fk>/", views.wishlist_delete, name="wishlist-delete"),

    path("phonemodels/", views.phones, name="phonemodels"),
]
