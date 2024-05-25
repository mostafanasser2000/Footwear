from django import forms
from orders.models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["email", "first_name", "last_name", "city", "address", "postal_code"]
