from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from core.models import Product, ProductItem
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST


class CartView(LoginRequiredMixin, TemplateResponseMixin, View):
    model = Cart
    template_name = "cart/detail.html"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=self.request.user)

        return self.render_to_response({"cart": cart})

    def post(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.POST.get("item_id")
        size = request.POST.get("size")
        color = request.POST.get("color")
        quantity = request.POST.get("quantity", 1)
        product_item = get_object_or_404(
            ProductItem, product=product_id, color=color, size=size
        )
        cart_item = CartItem.objects.create(cart=cart, item=product_item)
        try:
            quantity = int(quantity)
            if quantity <= 0:
                quantity = 1

        except ValueError:
            quantity = 1

        cart_item.quantity = quantity

        cart_item.save()
        return redirect("cart:user_cart")


@require_POST
def update_cart_item(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, pk=item_id, cart=cart)
    quantity = request.POST.get("quantity", 1)
    try:
        quantity = int(quantity)
        if quantity <= 0:
            quantity = 1

    except ValueError:
        quantity = 1

    cart_item.quantity = quantity

    cart_item.save()
    return redirect("cart:user_cart")


@require_POST
def remove_cart_item(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, pk=item_id, cart=cart)
    cart_item.delete()
    return redirect("cart:user_cart")
