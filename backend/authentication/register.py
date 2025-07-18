from django.contrib.auth import authenticate
# from authentication.models import User  # or use from django.contrib.auth.models
from django.contrib.auth.models import User

import os
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

import random


# 🧠 Helper function to generate a unique username
def generate_username(name):
    username = "".join(name.split(" ")).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        return generate_username(username + str(random.randint(0, 1000)))


# 🔁 This function handles Google login or signup
def register_social_user(provider, user_id, email, name):
    existing_users = User.objects.filter(email=email)

    if existing_users.exists():
        user = existing_users[0]

        if user.auth_provider == provider:
            # 🔐 Authenticate using default password
            registered_user = authenticate(
                email=email, password=settings.SOCIAL_SECRET
            )
            if not registered_user:
                raise AuthenticationFailed("Authentication failed.")

            return {
                "email": registered_user.email,
                "username": registered_user.username,
                "tokens": registered_user.tokens(),  # 👈 your User model must have a tokens() method
            }
        else:
            raise AuthenticationFailed(
                f"Please continue login using {user.auth_provider}"
            )

    else:
        # ✅ Create new user
        user = User.objects.create_user(
            username=generate_username(name),
            email=email,
            password=settings.SOCIAL_SECRET
        )
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        # 🔐 Login the new user
        new_user = authenticate(email=email, password=settings.SOCIAL_SECRET)
        return {
            "email": new_user.email,
            "username": new_user.username,
            "tokens": new_user.tokens()
        }
