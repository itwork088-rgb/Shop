# 🛍 Магазин электроники и одежды

## Описание проекта
Интернет-магазин на Django для продажи электроники и одежды.
Реализован каталог товаров, категории, корзина покупок.

---

## 🏗 Структура проекта

```
Shop/
├── shop/                    # Основной Django-проект
│   ├── settings.py         # Настройки проекта
│   ├── urls.py             # Главные маршруты
│   ├── wsgi.py             # WSGI-конфигурация
│   └── asgi.py             # ASGI-конфигурация
│
├── myshop/                  # Приложение "Магазин"
│   ├── models.py           # Модели Category, Product
│   ├── views.py            # Контроллеры (product_list, product_detail, category_products)
│   ├── urls.py             # Маршруты магазина
│   ├── admin.py            # Настройка админ-панели
│   └── templates/
│       └── home.html       # Главная страница каталога
│
├── cart/                    # Приложение "Корзина"
│   ├── cart.py             # Класс Cart (работа с сессией)
│   ├── views.py            # Контроллеры корзины (cart_detail, cart_add, cart_remove)
│   ├── urls.py             # Маршруты корзины
│   └── templates/
│       └── cart/           # (нужно создать cart_detail.html)
│           └── cart_detail.html
│
├── static/                  # Статические файлы
│   └── home.css            # Стили главной страницы
│
├── media/                   # Загруженные изображения товаров
├── .ai-docs/                # Документация
└── manage.py                # Утилита управления Django
```

---

## 📦 Модели данных

### Category (Категория)
| Поле | Тип | Описание |
|------|-----|----------|
| name | CharField(100) | Название категории |
| slug | SlugField(unique) | URL-метка |

### Product (Товар)
| Поле | Тип | Описание |
|------|-----|----------|
| category | ForeignKey(Category) | Категория товара |
| name | CharField(200) | Название товара |
| slug | SlugField(unique) | URL-метка |
| description | TextField | Описание товара |
| price | DecimalField(10,2) | Цена |
| image | ImageField | Фото товара |
| is_available | BooleanField(default=True) | В наличии |
| created_at | DateTimeField(auto_now_add) | Дата добавления |

---

## 🛒 Корзина (Cart)

Корзина реализована через Django-сессии:
- **Cart** — класс-обёртка над сессией
- **add(product, quantity)** — добавить товар
- **remove(product)** — удалить товар
- **get_total_price()** — общая стоимость
- **clear()** — очистить корзину

---

## ⚠ Найденные проблемы (нужно исправить)

1. **`home.html`** — используется `product.title`, должно быть `product.name`
2. **`home.html`** — нет ссылок на категории и корзину
3. **`views.py`** — указан шаблон `products/product_list.html`, но файл называется `home.html`
4. **`shop/urls.py`** — не подключены маршруты корзины `cart.urls`
5. **`static/home.css`** — `width:10;` должно быть `width:100%;`
6. **Нет шаблона** `cart/cart_detail.html` для страницы корзины
7. **Нет шаблона** `products/product_detail.html` для страницы товара

---

## 🔧 Технологии

- Python 3.x
- Django 5.2
- SQLite
- HTML5 / CSS3
- Google Fonts (Poppins)

