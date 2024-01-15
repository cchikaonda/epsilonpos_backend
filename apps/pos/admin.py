# admin.py in your 'your_app_name' app
from django.contrib import admin
from .models import Customer, Sale, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

class SaleAdmin(admin.ModelAdmin):
    inlines = [SaleItemInline]
    list_display = ('sale_date', 'total_amount')  # Add more fields as needed
    search_fields = ['sale_date']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'total_orders')
    search_fields = ['name', 'phone_number']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale, SaleAdmin)
