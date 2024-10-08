from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'buyer_name',
            'buyer_firstname',
            'delivery_address'
        ]