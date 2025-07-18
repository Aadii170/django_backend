from django.urls import path
from . import views


urlpatterns = [
    # path("create-payment/", views.payment_request, name="payment-request"),
    # path("success/", views.payment_successful, name="payment-successful"),
    path("", views.index, name="index"),
    path(
        "ccavResponseHandler",
        views.CCAVRequestHandler.as_view(),
        name="ccav-request-handler",
    ),
]
