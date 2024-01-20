# models.py in your 'inventory' app
from django.db import models
from django.utils import timezone
import uuid

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Batch(models.Model):
    AUTO_GENERATED = 'auto'
    MANUAL_ENTRY = 'manual'
    BATCH_NUMBER_CHOICES = [
        (AUTO_GENERATED, 'Auto-generated'),
        (MANUAL_ENTRY, 'Manual entry'),
    ]

    batch_number = models.CharField(
        max_length=50,
        unique=True,
        choices=BATCH_NUMBER_CHOICES,
        default=AUTO_GENERATED,
        help_text='Choose "Auto-generated" or "Manual entry"',
    )
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE, related_name='batches')
    manufacturing_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField()
    # Add more batch-related fields as needed

    def save(self, *args, **kwargs):
        if self.batch_number == self.MANUAL_ENTRY and not self.pk:
            # Only set a manual batch number if it's a new entry
            self.batch_number = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.batch_number} - {self.manufacturing_date}"

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateField()
    # Add more purchase-related fields as needed

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update quantity_in_stock of associated products
        for purchase_item in self.purchase_items.all():
            product = purchase_item.product
            product.receive_stock(purchase_item.quantity)

            # Explicitly call the save method for each related PurchaseItem
            purchase_item.save()

    def delete(self, *args, **kwargs):
        # Update quantity_in_stock of associated products before deletion
        for purchase_item in self.purchase_items.all():
            product = purchase_item.product
            product.quantity_in_stock -= purchase_item.quantity
            product.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.purchase_date)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='purchase_items')
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update quantity_in_stock of the associated product
        self.product.receive_stock(self.quantity)

    def __str__(self):
        return self.product.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
    path = models.CharField(max_length=255, null=True, blank=True, editable=False, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = str(self.pk)
        super().save(*args, **kwargs)

    def get_full_path(self):
        return self.path.split('/')

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def receive_stock(self, quantity):
        self.quantity_in_stock += quantity
        self.save()