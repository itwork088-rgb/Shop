from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def product_list(request):
    """Главная страница — все доступные товары"""
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    return render(
        request,
        "home.html",
        {"products": products, "categories": categories},
    )


def product_detail(request, slug):
    """Страница одного товара"""
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, "home.html", {"product": product})


def category_products(request, slug):
    """Товары одной категории"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_available=True)
    return render(
        request,
        "home.html",
        {"products": products, "categories": Category.objects.all(), "current_category": category},
    )
    

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer

PRODUCTS = [
    {"id": 1, "title": "Ноутбук", "price": 300000, "in_stock": True},
    {"id": 2, "title": "Мышка", "price": 7000, "in_stock": False},
    {"id": 3, "title": "Телефон", "price": 100000, "in_stock": True},
]


class ProductListAPIView(APIView):
    def get(self, request):
        serializer = ProductSerializer(PRODUCTS, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)