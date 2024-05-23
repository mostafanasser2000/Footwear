from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from core.models import Category, Product, ProductItem, Size, Brand
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


def home(request):
    return render(request, "core/home.html")


class ProductList(ListView):
    context_object_name = "products"
    template_name = "core/product/list.html"

    def get_queryset(self):
        qs = Product.objects.all()
        category = self.kwargs.get("category", "")
        size = self.kwargs.get("size", "")
        color = self.kwargs.get("color", "")

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
        return qs


class ProductDetail(DetailView):
    queryset = Product.objects.all()
    template_name = "core/product/detail.html"
    context_object_name = "product"
