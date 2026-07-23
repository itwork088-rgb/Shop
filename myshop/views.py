from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product, Review


def product_list(request):
    """Главная страница — все доступные товары с поиском и фильтрацией"""
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    # --- Поиск ---
    query = request.GET.get("q", "")
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # --- Фильтрация по цене ---
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(
        request,
        "home.html",
        {
            "products": products,
            "categories": categories,
            "query": query,
            "min_price": min_price,
            "max_price": max_price,
        },
    )


def product_detail(request, slug):
    """Страница одного товара с отзывами"""
    product = get_object_or_404(Product, slug=slug, is_available=True)
    reviews = product.reviews.all()

    if request.method == "POST" and request.user.is_authenticated:
        rating = int(request.POST.get("rating", 5))
        text = request.POST.get("text", "")
        if text:
            Review.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                text=text,
            )
            messages.success(request, "Отзыв добавлен!")
        return redirect("products:detail", slug=product.slug)

    return render(
        request,
        "products/product_detail.html",
        {"product": product, "reviews": reviews},
    )


def category_products(request, slug):
    """Товары одной категории с поиском и фильтрацией"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_available=True)

    # --- Поиск ---
    query = request.GET.get("q", "")
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # --- Фильтрация по цене ---
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(
        request,
        "home.html",
        {
            "products": products,
            "categories": Category.objects.all(),
            "current_category": category,
            "query": query,
            "min_price": min_price,
            "max_price": max_price,
        },
    )


# ====================== АВТОРИЗАЦИЯ ======================


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect("products:list")
        else:
            return render(
                request,
                "registration/login.html",
                {"form": None, "errors": True},
            )
    return render(request, "registration/login.html", {"form": None})


def user_logout(request):
    logout(request)
    messages.success(request, "Вы вышли из аккаунта.")
    return redirect("products:list")


def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect("products:list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def user_profile(request):
    orders = request.user.orders.all()
    return render(request, "registration/profile.html", {"orders": orders})


# ====================== REST API ======================

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

