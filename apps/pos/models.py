from pickle import FALSE
from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.shortcuts import reverse
from constance import config
from datetime import date

from djmoney.money import Money
from apps.accounts.models import CustomUser
from apps.stock.models import Supplier, Purchase, PurchaseItem, Product
from django.db.models.functions import Abs
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from . import mpamba_service_bill, airtel_service_bill

class Customer(models.Model):
    name = models.CharField(unique=True, max_length=120)
    phone_number = PhoneNumberField(null = True, blank = True)
    address = models.TextField(null=True)
    total_orders = models.IntegerField(default=0)

    def __str__(self):
        return '{0}'.format(self.name)
    
class Sale(models.Model):
    sale_date = models.DateField()
    total_amount = MoneyField(max_digits=10, decimal_places=2)  # Add relevant fields for sales

    # Add more sale-related fields as needed

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Add more sale item-related fields as needed

    def calculate_total_price(self):
        return self.quantity_sold * self.unit_price

class MobileTransactionFee(models.Model):
    amount_range_start = models.FloatField()
    amount_range_end = models.FloatField()
    fee = models.FloatField()

    def __str__(self):
        return f'{self.amount_range_start} - {self.amount_range_end}: {self.fee}'

