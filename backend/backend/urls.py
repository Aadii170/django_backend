# 📦 Main project URL configuration file

# ✅ Using Baton's custom admin panel instead of Django's default
from baton.autodiscover import admin
from django.urls import include, path

urlpatterns = [
    # 🛠️ Admin panel (customized with Baton)
    path("admin/", admin.site.urls),

    # 🎨 Baton admin UI assets
    path("baton/", include("baton.urls")),

    # 🔐 Authentication APIs (register, login, token, etc.)
    path("api/auth/", include("authentication.urls"), name="authentication"),

    # 🛍️ Store APIs (products, categories, etc.)
    path("api/store/", include("store.urls"), name="store"),

    # 🧾 Checkout & order placement
    path("api/checkout/", include("checkout.urls"), name="checkout"),

    # 🎨 Customization APIs (for personalized orders or items)
    path("api/customize/", include("customize.urls"), name="customize"),

    # 💬 Reviews & Ratings
    path("api/reviews/", include("reviews.urls"), name="reviews"),

    # 💳 Payment gateway integration (Razorpay, CCAvenue, Stripe)
    path("payments/", include("payments.urls"), name="payments"),

    # ❌ Feedback is currently disabled
    # path("api/feedback/", include("feedback.urls"), name="feedback"),

    # 🧪 Optional: Jet Admin (disabled for now)
    # path("jet/", include("jet.urls")),
    # path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
]
