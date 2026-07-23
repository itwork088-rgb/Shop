from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
from .models import Order, OrderItem


@login_required
def checkout(request):
    """Страница оформления заказа"""
    cart = Cart(request)
    if len(cart) == 0:
        return redirect("products:list")
    return render(request, "orders/checkout.html", {"cart": cart})


@login_required
def order_create(request):
    """Создание заказа из корзины"""
    cart = Cart(request)
    if len(cart) == 0:
        return redirect("products:list")

    if request.method == "POST":
        order = Order.objects.create(
            user=request.user,
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            address=request.POST["address"],
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                price=item["price"],
                quantity=item["quantity"],
            )
        cart.clear()
        messages.success(request, "Заказ успешно оформлен!")
        return redirect("orders:order_success", order_id=order.id)

    return redirect("orders:checkout")


@login_required
def order_success(request, order_id):
    """Страница успешного заказа"""
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, "orders/order_success.html", {"order": order})

