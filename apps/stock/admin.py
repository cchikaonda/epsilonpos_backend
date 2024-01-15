# admin.py in your 'inventory' app
from django.contrib import admin
from .models import Supplier, Purchase, PurchaseItem, Product, Batch, ProductCategory

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1

class BatchInline(admin.TabularInline):
    model = Batch
    extra = 1

class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'unit_cost', 'quantity', 'batch_number', 'purchase_date')

    def batch_number(self, obj):
        return obj.purchase.batches.first().batch_number if obj.purchase.batches.exists() else None

    def purchase_date(self, obj):
        return obj.purchase.purchase_date

    batch_number.short_description = 'Batch Number'
    purchase_date.short_description = 'Purchase Date'

class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchaseItemInline, BatchInline]
    list_display = ('supplier', 'purchase_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity_in_stock', 'created_at', 'updated_at')
    search_fields = ['name']

class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_number', 'purchase')
    search_fields = ['batch_number']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Supplier)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem, PurchaseItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
