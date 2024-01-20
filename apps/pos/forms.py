# forms.py in your app

from django import forms
from .models import MobileTransactionFee

class MobileTransactionFeeForm(forms.ModelForm):
    class Meta:
        model = MobileTransactionFee
        fields = '__all__'
