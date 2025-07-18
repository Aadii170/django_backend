from django.urls import path
from .views import signup, login_view
from .views import GoogleSocialAuthView  # 👈 Google login view import karo

urlpatterns = [
    path("signup/", signup, name="signup"),           # 🔐 Normal user signup
    path("login/", login_view, name="login"),         # 🔐 Normal user login
    path("google-login/", GoogleSocialAuthView.as_view(), name="google-login"),  # 🔐 Google se login
]
