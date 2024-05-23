from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from core.models import Product, ProductItem
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin


class CartView(TemplateResponseMixin, View, LoginRequiredMixin):
    model = Cart
    template_name = "cart/detail.html"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=self.request.user)

        return self.render_to_response({"cart": cart})

    def post(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_item_id = request.POST.get("item_id")
        quantity = request.POST.get("quantity", 1)
        product_item = get_object_or_404(ProductItem, pk=product_item_id)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, item=product_item
        )
        try:
            quantity = int(quantity)
            if quantity <= 0:
                quantity = 1

        except ValueError:
            quantity = 1

        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        return redirect("cart:user_cart")
