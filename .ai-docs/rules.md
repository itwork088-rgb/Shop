# 📐 Правила и стандарты проекта

## 🎯 Целевые категории товаров
1. **Электроника** — смартфоны, ноутбуки, наушники, аксессуары
2. **Одежда** — кроссовки, футболки, куртки, аксессуары

---

## 🔤 Соглашения по коду

### Именование
- **Модели** — `PascalCase` (Product, Category)
- **Функции/методы** — `snake_case` (product_list, get_total_price)
- **Переменные** — `snake_case` (product_id, cart_item)
- **URL-имена** — `kebab-case` или `snake_case`

### Django-стандарты
- `app_name = "products"` для namespace
- `verbose_name` / `verbose_name_plural` на русском
- Slug для URL идентификации (не id)

### Шаблоны
- Папки шаблонов по имени приложения: `myshop/templates/`, `cart/templates/cart/`
- Шаблон: `home.html`, `cart_detail.html`, `product_detail.html`

---

## 🚀 Порядок разработки

### Установка
```bash
python -m venv venv
venv\Scripts\activate
pip install django pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ✅ Чек-лист завершённости фичи

- [ ] Модель создана и зарегистрирована в admin.py
- [ ] Выполнены миграции
- [ ] Созданы view-функции
- [ ] Настроены URL-маршруты
- [ ] Создан HTML-шаблон
- [ ] Добавлены стили (если нужно)
- [ ] Протестировано в браузере

