"""
Кастомная команда для заполнения БД тестовыми данными.
Запуск: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from myshop.models import Category, Product


class Command(BaseCommand):
    help = "Заполняет базу тестовыми товарами (электроника + одежда)"

    def handle(self, *args, **options):
        self.stdout.write("Заполняю базу данных...")

        # --- Категории ---
        electronics, _ = Category.objects.get_or_create(
            name="Электроника",
            slug="electronics"
        )
        clothing, _ = Category.objects.get_or_create(
            name="Одежда",
            slug="clothing"
        )
        self.stdout.write(self.style.SUCCESS("✓ Категории созданы"))

        # --- Товары: Электроника ---
        electronics_products = [
            {
                "name": "iPhone 15 Pro Max",
                "slug": "iphone-15-pro-max",
                "description": "Флагманский смартфон Apple с титановым корпусом, чипом A17 Pro и 48-Мп камерой.",
                "price": 119990,
                "image": "2026/07/21/1_98bb4fc0-bf85-477c-b338-90bb6f2e9ab5.webp",
            },
            {
                "name": "Samsung Galaxy S24 Ultra",
                "slug": "samsung-galaxy-s24-ultra",
                "description": "Мощный смартфон с S Pen, 200-Мп камерой и процессором Snapdragon 8 Gen 3.",
                "price": 109990,
                "image": "2026/07/21/1_353aad53-b809-446e-9386-89e1dae6374b.webp",
            },
            {
                "name": "MacBook Air M3",
                "slug": "macbook-air-m3",
                "description": "Ноутбук Apple с чипом M3, 15-дюймовым дисплеем и до 18 часов работы.",
                "price": 149990,
                "image": "2026/07/21/macbook-air-m3.jpg",
            },
            {
                "name": "Sony WH-1000XM5",
                "slug": "sony-wh-1000xm5",
                "description": "Беспроводные наушники с активным шумоподавлением и высоким качеством звука.",
                "price": 34990,
                "image": "2026/07/21/sony-wh-1000xm5.jpg",
            },
            {
                "name": "Apple Watch Ultra 2",
                "slug": "apple-watch-ultra-2",
                "description": "Умные часы для экстремальных условий с дисплеем 3000 нит и GPS.",
                "price": 79990,
                "image": "2026/07/21/566-wt2.jpg",
            },
        ]

        for item in electronics_products:
            Product.objects.get_or_create(
                slug=item["slug"],
                defaults={
                    "category": electronics,
                    "name": item["name"],
                    "description": item["description"],
                    "price": item["price"],
                    "is_available": True,
                    "image": item.get("image", ""),
                },
            )
        self.stdout.write(self.style.SUCCESS(f"✓ Добавлено {len(electronics_products)} товаров электроники"))

        # --- Товары: Одежда ---
        clothing_products = [
            {
                "name": "Nike Air Jordan 1 Banned",
                "slug": "nike-air-jordan-1-banned",
                "description": "Легендарные кроссовки Nike Air Jordan 1 High 'Banned'. Классика в чёрно-красном цвете.",
                "price": 29990,
                "image": "2026/07/18/Air_Jordan_1_Banned.jpg",
            },
            {
                "name": "New Balance 1906R",
                "slug": "new-balance-1906r",
                "description": "Стильные кроссовки New Balance 1906R в ретро-стиле с современными технологиями.",
                "price": 15990,
                "image": "2026/07/21/NB-7280_MenShoesLS_1906_Image3.jpg",
            },
            {
                "name": "Nike Free Metcon 7 AMP",
                "slug": "nike-free-metcon-7-amp",
                "description": "Кроссовки для тренировок Nike Free Metcon 7 AMP — гибкость и поддержка.",
                "price": 13990,
                "image": "2026/07/21/NIKEFREEMETCON7AMP.avif",
            },
            {
                "name": "Suede Classic Sneakers",
                "slug": "suede-classic-sneakers",
                "description": "Классические замшевые кеды — универсальный выбор для повседневного стиля.",
                "price": 8990,
                "image": "2026/07/21/Suede-Classic-Sneakers.avif",
            },
            {
                "name": "Футболка Nike Dri-FIT",
                "slug": "nike-dri-fit-tshirt",
                "description": "Спортивная футболка Nike Dri-FIT с технологией отвода влаги. Чёрная.",
                "price": 4990,
                "image": "2026/07/21/nike-dri-fit.jpg",
            },
        ]

        for item in clothing_products:
            Product.objects.get_or_create(
                slug=item["slug"],
                defaults={
                    "category": clothing,
                    "name": item["name"],
                    "description": item["description"],
                    "price": item["price"],
                    "is_available": True,
                    "image": item.get("image", ""),
                },
            )
        self.stdout.write(self.style.SUCCESS(f"✓ Добавлено {len(clothing_products)} товаров одежды"))

        self.stdout.write(self.style.SUCCESS("✅ База данных успешно заполнена!"))

