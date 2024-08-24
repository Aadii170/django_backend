from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Customize
from .serializers import CustomizeSerializer

from checkout.models import Order
from checkout.serializers import OrderSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def customize(request):
    user = request.user
    image = request.FILES.get("image")
    name_on_cover = request.data.get("name_on_cover")
    quantity = request.data.get("quantity")
    ammount = request.data.get("ammount")
    phone = request.data.get("phone")
    phone_model = request.data.get("phone_model")
    customize = Customize.objects.create(
        user=user,
        image=image,
        name_on_cover=name_on_cover,
        quantity=quantity,
        ammount=ammount,
        phone=phone,
        phone_model=phone_model,
    )
    try:
        serializer = CustomizeSerializer(customize, many=False)
        return Response(serializer.data, status=200)
    except:
        return Response({"detail": "Something went wrong"}, status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def custom_order_checkout(request):
    user = request.user

    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            user=user,
            is_custom=True,
            name_on_cover=request.data.get("name_on_cover"),
            image=request.data.get("image"),
        )
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)
