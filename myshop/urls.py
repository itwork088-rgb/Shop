from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="list"),
    path("category/<slug:slug>/", views.category_products, name="category"),
    # Авторизация
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register"),
    # Профиль
    path("profile/", views.user_profile, name="profile"),
    # Детальная страница товара — ДОЛЖНА быть ПОСЛЕДНЕЙ
    path("<slug:slug>/", views.product_detail, name="detail"),
]

