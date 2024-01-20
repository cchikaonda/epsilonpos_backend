# urls.py in your 'inventory' app
from django.urls import path
from .views import (
    SupplierListView,
    SupplierDetailView,
    PurchaseListView,
    PurchaseDetailView,
    PurchaseItemListView,
    PurchaseItemDetailView,
    ProductListView,
    ProductDetailView,
    ProductCategoryListView,
    ProductCategoryDetailView,
    BatchListView,
    BatchDetailView,
)

urlpatterns = [
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('purchase-items/', PurchaseItemListView.as_view(), name='purchase-item-list'),
    path('purchase-items/<int:pk>/', PurchaseItemDetailView.as_view(), name='purchase-item-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product-categories/', ProductCategoryListView.as_view(), name='product-category-list'),
    path('product-categories/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),
    path('batches/', BatchListView.as_view(), name='batch-list'),
    path('batches/<int:pk>/', BatchDetailView.as_view(), name='batch-detail'),
]
