# views.py in your 'inventory' app
from rest_framework import generics
from .models import Supplier, Purchase, PurchaseItem, Product, ProductCategory, Batch
from .serializers import (
    SupplierSerializer,
    PurchaseSerializer,
    PurchaseItemSerializer,
    ProductSerializer,
    ProductCategorySerializer,
    BatchSerializer,
)

class SupplierListView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class PurchaseListView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseItemListView(generics.ListCreateAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer

class PurchaseItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryListView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class BatchListView(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
