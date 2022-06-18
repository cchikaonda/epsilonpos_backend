from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django import forms

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from constance.admin import ConstanceAdmin, ConstanceForm, Config

from accounts.models import CustomUser
from stock.models import Stock, Supplier, Item, ItemCategory, Unit, BatchNumber

# Register your models here.
CustomUser = get_user_model()

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'description')
    search_fields = ['name']

    class Meta:
        model = Supplier


admin.site.register(Supplier, SupplierAdmin)


class CustomConfigForm(ConstanceForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
         #... do stuff to make your settings form nice ...
    

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description','category_colour')
    search_fields = ['category_name', ]

    class Meta:
        model = ItemCategory
admin.site.register(ItemCategory, ItemCategoryAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'unit_short_name', 'unit_description',
        )
    search_fields = ['unit_short_name', ]
    class Meta:
        model = Unit
admin.site.register(Unit, UnitAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'barcode','item_name','get_cost_price','cost_price', 'get_total_cost_price','total_cost_price','price', 'selling_price', 'discount_price',
        'category',
        'item_description', 'slug','quantity_at_hand', 'active', 'unit','image'
        )
    search_fields = ['item_name', ]
    class Meta:
        model = Item
admin.site.register(Item, ItemAdmin)


class BatchNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'batch_number', 'batch_number_description', 'created_at')
    search_fields = ['batch_number']

    class Meta:
        model = BatchNumber


admin.site.register(BatchNumber, BatchNumberAdmin)


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'batch','item', 'supplier_name', 'ordered_price', 'previous_quantity',
        'stock_in','unit_quantity','get_total_stock','new_quantity','total_cost_of_items','created_at','updated_at')
    search_fields = ['item__item_name', ]
    class Meta:
        model = Stock
admin.site.register(Stock, StockAdmin)
