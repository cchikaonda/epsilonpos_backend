from dataclasses import field
from rest_framework import serializers
from .models import ItemCategory, Unit, Item, Supplier, Stock, BatchNumber


class SuppliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'id',
            'name',
            'address',
            'phone_number',
            'description',
        )

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = (
            'id',
            'unit_short_name',
            'unit_description',
        )

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = (
            'id',
            'category_name',
            'category_description',
            'category_colour',
        )

class ItemSerializer(serializers.ModelSerializer):
    # selling_price = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = [
             'id',
            'item_name',
            'item_description',
            'unit',
            'barcode',
            'get_image',
            'cost_price',
            'total_cost_price',
            'price_currency',
            # 'selling_price',
            # 'currency_selling_price',
            'price',
            'discount_price',
            'discount_price',
            'category',
            'quantity_at_hand',
            'reorder_level',
            'active',
            'slug',
        ]
           

        

class BatchNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchNumber
        fields = (
            'id',
            'batch_number',
            'batch_number_description',
            'created_at',

        )
