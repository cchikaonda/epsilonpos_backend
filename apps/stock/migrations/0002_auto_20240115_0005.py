# stock/migrations/000X_populate_categories_and_products.py
import os
from django.db import migrations
import json
from apps.stock.models import ProductCategory, Product

def create_categories_recursively(parent_category, subcategories_data):
    ProductCategory = parent_category.__class__

    for subcategory_data in subcategories_data:
        subcategory = ProductCategory.objects.create(name=subcategory_data['name'], parent_category=parent_category)
        if 'subcategories' in subcategory_data:
            create_categories_recursively(subcategory, subcategory_data['subcategories'])

def create_products_for_category(category, products_data):
    for product_data in products_data:
        Product.objects.create(
            name=product_data['name'],
            description=product_data['description'],
            quantity_in_stock=product_data.get('quantity_in_stock', 0),
            category=category
        )

def load_categories_and_products_from_json(apps, schema_editor):
    ProductCategory = apps.get_model('stock', 'ProductCategory')
    Product = apps.get_model('stock', 'Product')

    # Get the path to the current file
    current_file_path = os.path.abspath(__file__)

    # Build the path to the products.json file
    products_json_path = os.path.join(os.path.dirname(current_file_path), 'initial_data', 'products.json')

    with open(products_json_path, 'r') as file:
        categories_data = json.load(file)

    for category_data in categories_data:
        category = ProductCategory.objects.create(name=category_data['name'])
        if 'subcategories' in category_data:
            create_categories_recursively(category, category_data['subcategories'])

        if 'products' in category_data:
            create_products_for_category(category, category_data['products'])

class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_categories_and_products_from_json),
    ]
