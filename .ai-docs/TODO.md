# TODO: Реализация новых фич

## ✅ Шаг 1: Счётчик товаров в корзине (context processor)
- [x] Создать `cart/context_processors.py`
- [x] Подключить в `settings.py`
- [x] Обновить шапку в `home.html`, `product_detail.html`, `cart_detail.html`

## ✅ Шаг 2: Поиск по товарам
- [x] View `product_search` в `myshop/views.py`
- [x] URL `/search/` в `myshop/urls.py`
- [x] Форма поиска в `home.html`
- [x] Стили для поиска в `home.css`

## ✅ Шаг 3: Фильтрация по цене
- [x] Модифицировать `product_list` и `category_products` для фильтрации по цене
- [x] Форма фильтра в `home.html`
- [x] Стили для фильтра

## ✅ Шаг 4: Отзывы на товары
- [x] Модель `Review` в `myshop/models.py`
- [x] Миграция
- [x] View для отзывов (добавление + отображение)
- [x] Обновить `product_detail.html`
- [x] Зарегистрировать в `admin.py`
- [x] Стили для отзывов

## ✅ Шаг 5: Регистрация / Авторизация
- [x] URL-маршруты для login/logout/register
- [x] Views: `user_login`, `user_logout`, `user_register`
- [x] Шаблоны: `registration/login.html`, `registration/register.html`
- [x] Ссылки в шапке всех страниц

## ✅ Шаг 6: Личный кабинет
- [x] View `user_profile`
- [x] URL `/profile/`
- [x] Шаблон `registration/profile.html`
- [x] Стили для профиля

## ✅ Шаг 7: Оформление заказа (Checkout)
- [x] Создать приложение `orders`
- [x] Модели `Order` и `OrderItem`
- [x] Миграция
- [x] View `checkout`, `order_create`
- [x] URL `/cart/checkout/`
- [x] Шаблон `checkout.html`
- [x] Страница успешного заказа
- [x] Стили для заказа

## ✅ Шаг 8: Улучшенная мобильная версия
- [x] Burger-menu для навигации
- [x] Адаптивные стили для всех новых элементов
- [x] Проверка совместимости со старыми стилями

