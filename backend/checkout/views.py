from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CartItem, Order
from store.models import Products
from .serializers import CartItemSerializer, OrderSerializer

# Create your views here.


# cart views
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def cart(request):
    if request.method == "GET":
        cart = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "POST":
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_cart_item(request, fk):
    cart = CartItem.objects.get(product_id=fk, user=request.user)
    cart.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# order views here
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def place_order(request):
    cart = CartItem.objects.filter(user=request.user)
    if cart is not None:
        total = 0
        items = []
        for item in cart:
            items.append(item.product_id.id)
            total += item.product_id.price

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, items=items, total=total)
            for product in cart:  # deleting purchased products from cart
                product.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if cart is None:
        return Response("Cart is empty", status=status.HTTP_400_BAD_REQUEST)

    # cart = Cart.objects.get(user=request.user)
    # if cart is not None:
    #     cart.checkout = True
    #     cart.save()
    #     items = cart.items

    #     total = 0
    #     for item in items:
    #         product = Products.objects.get(id=item)
    #         total += product.price

    #     serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user, items=items, total=total)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # else:
    #     item = Products.objects.get(id=request.data["items"])
    #     total = item.price
    #     serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user, items=item, total=total)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
