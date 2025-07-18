from google.auth.transport import requests
from google.oauth2 import id_token
from django.conf import settings

class Google:
    @staticmethod
    def validate(auth_token):
        try:
            # Verifies token using Google public keys
            idinfo = id_token.verify_oauth2_token(
                auth_token,
                requests.Request(),
                settings.GOOGLE_CLIENT_ID
            )
            return idinfo
        except Exception as e:
            print("Google token verification failed:", e)
            return None
