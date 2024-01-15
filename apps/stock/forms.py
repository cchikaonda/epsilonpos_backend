# forms.py in your 'inventory' app
from django import forms
from .models import Batch

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the widget for the batch_number field based on the choice
        if self.instance and self.instance.batch_number == Batch.MANUAL_ENTRY:
            self.fields['batch_number'].widget = forms.TextInput(attrs={'placeholder': 'Enter Manual Batch Number'})
            self.fields['batch_number'].required = True
        else:
            self.fields['batch_number'].widget = forms.HiddenInput()
            self.fields['batch_number'].required = False

# admin.py in your 'inventory' app
from django.contrib import admin
from .models import Supplier, Purchase, PurchaseItem, Product, Batch, ProductCategory
from .forms import BatchForm

# forms.py in your 'inventory' app
from django import forms
from .models import Batch

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the widget for the batch_number field based on the choice
        if self.instance and self.instance.batch_number == Batch.MANUAL_ENTRY:
            self.fields['batch_number'].widget = forms.TextInput(attrs={'placeholder': 'Enter Manual Batch Number'})
        else:
            self.fields['batch_number'].widget = forms.HiddenInput()
            self.fields['batch_number'].required = False


admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.register(Product)
admin.site.register(Batch, BatchAdmin)
admin.site.register(ProductCategory)
