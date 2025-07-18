from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Categories, SubCategories, Products, Wishlist, Phones
from .serializers import (
    CategoriesSerializer,
    SubCategoriesSerializer,
    ProductsSerializer,
    WishlistSerializer,
    PhonesSerializer,
)


# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Categories": "/categories/",
        "SubCategories": "/subcategories/",
        "Products": "/products/",
    }
    return Response(api_urls)


@api_view(["GET"])
def categories(request, name):
    products = Products.objects.filter(category__name=name)
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def subcategories(request, name):
    products = Products.objects.filter(subcategory=name)
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def category_products(request, fk):
    products = Products.objects.filter(subcategory=fk)
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def products(request, pk):
    product = Products.objects.get(id=pk)
    serializer = ProductsSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def search(request, query):
    products = Products.objects.filter(name__icontains=query)
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def wishlist(request):
    if request.method == "GET":
        wishlist = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlist, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data)



@api_view(["DELETE"])
def wishlist_delete(request, fk):
    wishlist = Wishlist.objects.get(product=fk)
    wishlist.delete()
    return Response("Item removed from wishlist")


# phone mmodel views
@api_view(["GET"])
def phones(request):
    phones = Phones.objects.all()
    serializer = PhonesSerializer(phones, many=True)
    return Response(serializer.data)
