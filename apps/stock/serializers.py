# serializers.py in your 'inventory' app
from rest_framework import serializers
from .models import Supplier, Purchase, PurchaseItem, Product, ProductCategory, Batch

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class PurchaseItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()  # Use StringRelatedField to display the 'name' field of the related Product

    class Meta:
        model = PurchaseItem
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    purchase_items = PurchaseItemSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    parent_category_name = serializers.StringRelatedField(source='category.parent_category', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

