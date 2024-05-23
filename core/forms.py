from django.forms import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "image", "description", "price"]
