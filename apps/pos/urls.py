# urls.py in your 'sales' app
from django.urls import path
from .views import (
    CustomerListCreateView, CustomerDetailView,
    SaleListCreateView, SaleDetailView,
    SaleItemListCreateView, SaleItemDetailView,
    mobile_transaction_fee_view,
)

urlpatterns = [
    path('mobile-transaction-fees/', mobile_transaction_fee_view, name='mobile_transaction_fee_view'),
    path('customers/', CustomerListCreateView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),

    path('sales/', SaleListCreateView.as_view(), name='sale_list'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name='sale_detail'),

    path('saleitems/', SaleItemListCreateView.as_view(), name='saleitem_list'),
    path('saleitems/<int:pk>/', SaleItemDetailView.as_view(), name='saleitem_detail'),
]
