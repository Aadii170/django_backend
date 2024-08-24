# from django.contrib import admin
from baton.autodiscover import admin
from django.urls import include, path

urlpatterns = [
    # path("jet/", include("jet.urls")),
    # path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
    path("api/auth/", include("authentication.urls"), name="authentication"),
    path("api/store/", include("store.urls"), name="store"),
    path("api/checkout/", include("checkout.urls"), name="checkout"),
    path("api/customize/", include("customize.urls"), name="customize"),
    # path("api/feedback/", include("feedback.urls"), name="feedback"),
    path("api/reviews/", include("reviews.urls"), name="reviews"),
    path("payments/", include("payments.urls"), name="payments"),
]
