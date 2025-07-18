from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes

from .models import Review
from .serializers import ReviewSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_review_list_create(request, product_id=None):
    if request.method == "GET":
        if product_id is not None:
            reviews = Review.objects.filter(product_id=product_id)
            if not reviews.exists():
                return Response(
                    {"error": "No reviews found for the specified product."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"error": "Product ID must be provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
