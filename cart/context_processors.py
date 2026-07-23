from .cart import Cart


def cart_context(request):
    """Добавляет объект корзины и количество товаров в контекст шаблона"""
    cart = Cart(request)
    return {
        "cart": cart,
        "cart_total_items": len(cart),
    }

