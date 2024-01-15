# urls.py in your 'inventory' app
from django.urls import path
from .views import (
    SupplierListCreateView, SupplierDetailView,
    PurchaseListCreateView, PurchaseDetailView,
    PurchaseItemListCreateView, PurchaseItemDetailView,
    ProductListCreateView, ProductDetailView
)

urlpatterns = [
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),

    path('purchases/', PurchaseListCreateView.as_view(), name='purchase_list'),
    path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),

    path('purchaseitems/', PurchaseItemListCreateView.as_view(), name='purchaseitem_list'),
    path('purchaseitems/<int:pk>/', PurchaseItemDetailView.as_view(), name='purchaseitem_detail'),

    path('products/', ProductListCreateView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
