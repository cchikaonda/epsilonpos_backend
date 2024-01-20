# views.py in your 'sales' app
from rest_framework import generics
from .models import Customer, Sale, SaleItem
from .serializers import CustomerSerializer, SaleSerializer, SaleItemSerializer

# views.py in your app

from django.shortcuts import render, redirect
from .forms import MobileTransactionFeeForm
from constance import config

# views.py in your app

from django.shortcuts import render, redirect
from .forms import MobileTransactionFeeForm

def mobile_transaction_fee_view(request):
    form = MobileTransactionFeeForm()

    if request.method == 'POST':
        form = MobileTransactionFeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Assuming you have a success_page defined in your URLs
            return redirect('success_page')

    return render(request, 'mobile_transaction_fee_form.html', {'form': form})


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleItemListCreateView(generics.ListCreateAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer

class SaleItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
