from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from core.models import Category, Product, ProductItem, Size, Color, Brand
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


class ProductList(ListView):
    context_object_name = "products"
    template_name = "core/home.html"

    def get_queryset(self):
        qs = Product.objects.all()
        category = self.kwargs.get("category", "")
        size = self.kwargs.get("size", "")
        color = self.kwargs.get("color", "")
        gender = self.kwargs.get("gender", "")
        q = self.request.GET.get("q", "")
        if category:
            qs = qs.filter(Q(category__slug=category) | Q(category__name=category))
        if size:
            qs = qs.filter(
                id__in=ProductItem.objects.filter(size__slug=size)
                .values("product")
                .distinct()
            )
        if color:
            qs = qs.filter(
                id__in=ProductItem.objects.filter(color__slug=color)
                .values("product")
                .distinct()
            )
        if gender:
            qs = qs.filter(gender=gender)
        

        if q:
            qs = qs.filter(name__icontains=q)
        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        sizes = Size.objects.all()
        colors = Color.objects.all()
        brands = Brand.objects.all()
        context["categories"] = categories
        context["sizes"] = sizes
        context["colors"] = colors
        context["brands"] = brands
        return context


class ProductDetail(DetailView):
    queryset = Product.objects.all()
    template_name = "core/product/detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        obj = self.get_object()
        context = super().get_context_data(**kwargs)
        available_sizes = Size.objects.filter(
            id__in=ProductItem.objects.filter(product=obj).values("size")
        )
        available_colors = Color.objects.filter(
            id__in=ProductItem.objects.filter(product=obj).values("color")
        )
        context["available_sizes"] = available_sizes
        context["available_colors"] = available_colors
        return context
