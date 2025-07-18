from rest_framework import status

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer  , GoogleSocialAuthSerializer

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        user = User.objects.get(username=serializer.data["username"])
        token = Token.objects.create(user=user)
        return Response(
            {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_view(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        # print("1")
        user = authenticate(request, username=username, password=password)
        # print("2")


        if user:
            # print("3")
            login(request=request, user=user)
            # print("4")
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# 🔐 Login with Google - POST endpoint
class GoogleSocialAuthView(GenericAPIView):

    # 👇 Is view me yeh serializer use hoga (jisme auth_token validate hota hai)
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        # ✅ Step 1: Request data ko serializer me daalo
        serializer = self.serializer_class(data=request.data)

        # ✅ Step 2: Validate karo token ko
        # Agar token galat hoga ya expire hoga, toh yahin exception aayega
        serializer.is_valid(raise_exception=True)

        # ✅ Step 3: Agar sab sahi hai, toh validated_data return karega
        # Isme hoga: email, username, tokens (access/refresh)
        user_data = serializer.validated_data

        # ✅ Step 4: Frontend ko response bhejna (token + user info)
        return Response(user_data, status=status.HTTP_200_OK)