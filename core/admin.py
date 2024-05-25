from django.contrib import admin
from .models import Product, Category, Brand, Color, Size, ProductItem
from django import forms


class ProductAdminForm(forms.ModelForm):
    available_sizes = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(), required=False
    )
    available_colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(), required=False
    )

    class Meta:
        model = Product
        fields = "__all__"

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()

        sizes = self.cleaned_data.get("available_sizes")
        colors = self.cleaned_data.get("available_colors")

        for size in sizes:
            for color in colors:
                ProductItem.objects.create(product=instance, size=size, color=color)

        return instance


class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "name",
        "slug",
        "price",
    ]
    list_filter = ['category']
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductItemInline]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)
