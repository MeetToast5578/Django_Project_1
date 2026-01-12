from django.core.management.base import BaseCommand
from product.models import Product, ProductCategory, ProductTag
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Creates sample products based on static images'

    def handle(self, *args, **kwargs):
        # Create categories
        handmade_cat, _ = ProductCategory.objects.get_or_create(
            title='Handmade Crafts',
            parent=None
        )
        home_decor_cat, _ = ProductCategory.objects.get_or_create(
            title='Home Decor',
            parent=None
        )
        kitchen_cat, _ = ProductCategory.objects.get_or_create(
            title='Kitchen & Dining',
            parent=None
        )
        art_cat, _ = ProductCategory.objects.get_or_create(
            title='Art & Paintings',
            parent=None
        )

        # Create tags
        new_tag, _ = ProductTag.objects.get_or_create(title='New')
        handmade_tag, _ = ProductTag.objects.get_or_create(title='Handmade')
        wooden_tag, _ = ProductTag.objects.get_or_create(title='Wooden')
        ceramic_tag, _ = ProductTag.objects.get_or_create(title='Ceramic')

        # Products data matching the static images
        products_data = [
            {
                'title': 'Hand-Made Garlic Mortar',
                'price': '38.50',
                'description': 'Beautiful handmade garlic mortar crafted from natural materials. Perfect for crushing herbs and spices.',
                'category': kitchen_cat,
                'cover_image': 'product_images/1.jpg',
                'tags': [handmade_tag, wooden_tag, new_tag]
            },
            {
                'title': 'Handmade Ceramic Pottery',
                'price': '38.50',
                'description': 'Elegant handmade ceramic pottery piece. Perfect for your home decoration or as a unique gift.',
                'category': home_decor_cat,
                'cover_image': 'product_images/2.jpg',
                'tags': [handmade_tag, ceramic_tag, new_tag]
            },
            {
                'title': 'Hand Painted Bowls',
                'price': '38.50',
                'description': 'Beautifully hand-painted bowls with intricate designs. Each piece is unique.',
                'category': kitchen_cat,
                'cover_image': 'product_images/3.jpg',
                'tags': [handmade_tag, ceramic_tag]
            },
            {
                'title': 'Antique Wooden Farm Large',
                'price': '38.50',
                'description': 'Large antique wooden farm piece. Adds rustic charm to any space.',
                'category': home_decor_cat,
                'cover_image': 'product_images/4.jpg',
                'tags': [wooden_tag, handmade_tag]
            },
            {
                'title': 'Handmade Jute Basket',
                'price': '38.50',
                'description': 'Eco-friendly handmade jute basket. Perfect for storage and organization.',
                'category': home_decor_cat,
                'cover_image': 'product_images/6.jpg',
                'tags': [handmade_tag, new_tag]
            },
            {
                'title': 'Knitting Yarn & Crochet Hook',
                'price': '38.50',
                'description': 'High-quality knitting yarn with crochet hook. Perfect for your crafting projects.',
                'category': handmade_cat,
                'cover_image': 'product_images/7.jpg',
                'tags': [handmade_tag, new_tag]
            },
            {
                'title': 'David Head Portraits',
                'price': '38.50',
                'description': 'Beautiful artistic portrait of David. Perfect for art lovers.',
                'category': art_cat,
                'cover_image': 'product_images/8.jpg',
                'tags': [new_tag]
            },
            {
                'title': 'Solid Wood Cherry Paddle',
                'price': '38.50',
                'description': 'Premium solid wood cherry paddle. Handcrafted with attention to detail.',
                'category': kitchen_cat,
                'cover_image': 'product_images/9.jpg',
                'tags': [wooden_tag, handmade_tag]
            },
            {
                'title': 'Vintage Wooden Spoon Set',
                'price': '42.00',
                'description': 'Set of vintage wooden spoons. Perfect for cooking and serving.',
                'category': kitchen_cat,
                'cover_image': 'product_images/10.jpg',
                'tags': [wooden_tag, handmade_tag]
            },
            {
                'title': 'Decorative Wall Hanging',
                'price': '45.00',
                'description': 'Unique decorative wall hanging. Adds personality to any room.',
                'category': home_decor_cat,
                'cover_image': 'product_images/11.jpg',
                'tags': [handmade_tag, new_tag]
            },
            {
                'title': 'Artisan Ceramic Vase',
                'price': '52.00',
                'description': 'Handcrafted artisan ceramic vase. Perfect for fresh or dried flowers.',
                'category': home_decor_cat,
                'cover_image': 'product_images/12.jpg',
                'tags': [ceramic_tag, handmade_tag, new_tag]
            },
        ]

        # Create products
        created_count = 0
        for product_data in products_data:
            tags = product_data.pop('tags')
            
            # Check if product already exists
            if not Product.objects.filter(title=product_data['title']).exists():
                product = Product.objects.create(**product_data)
                product.tags.set(tags)
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product_data["title"]}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} products!'))
