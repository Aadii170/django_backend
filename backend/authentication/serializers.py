from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from authentication.register import register_social_user  # ✅ Google login ya signup handle karne wali file
import os

from . import google  # ✅ Google ka token verify karne wali file

# ✅ Ye basic UserSerializer hai jo username aur password handle karta hai
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ("username", "password")

    # username required hoga
    username = serializers.CharField(required=True)

    # password bhi required hai aur sirf likhne ke liye (write_only)
    password = serializers.CharField(required=True, write_only=True)


# 🔐 Google login ke liye serializer
# Yeh frontend se aane wale Google ke token ko verify karta hai
class GoogleSocialAuthSerializer(serializers.Serializer):
    # auth_token = Google ka ID token jo frontend se aata hai
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        # ✅ Step 1: Google ke server se token verify karo
        user_data = google.Google.validate(auth_token)

        # ❌ Step 2: Check karo ki token valid hai ya expire ho gaya
        try:
            user_data['sub']  # 'sub' = Google ka unique user ID
        except:
            raise serializers.ValidationError(
                'Token invalid ya expire ho gaya. Dobara login karo.'
            )

        # ❌ Step 3: Check karo ki yeh token hamare app ke liye hi bana tha
        # 'aud' = audience yaani token kis app ke liye issue hua
        if user_data['aud'] != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed('Oops! Yeh token hamare app ka nahi hai.')

        # ✅ Step 4: Google se mila hua data extract karo
        user_id = user_data['sub']  # Google ka unique ID
        email = user_data['email']  # User ka email
        name = user_data.get('name', email.split('@')[0])  # Agar naam na mile toh email ka pehla part use karo
        provider = 'google'  # batata hai ki yeh login Google se ho raha hai

        # ✅ Step 5: register ya login karo user ko
        # Yeh function check karega ki user already exist karta hai ya nahi
        return register_social_user(
            provider=provider,
            user_id=user_id,
            email=email,
            name=name
        )
