from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View, TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Cart, CartItem
from orders.forms import OrderCreateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from orders.models import Order, OrderItem


@login_required
def order_create(request):
    cart = Cart.objects.get(user=request.user)

    if cart.items.count() == 0:
        return redirect(reverse("core:product_list"))

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    item=cart_item.item,
                    price=cart_item.unit_price,
                    quantity=cart_item.quantity,
                )

                cart_item.delete()
        return redirect(reverse("orders:order_complete", kwargs={"order_id": order.id}))
    else:
        form = OrderCreateForm()
    return render(request, "orders/order/create.html", {"cart": cart, "form": form})


@login_required
def order_complete(request, order_id):
    order = get_object_or_404(Order, user=request.user, pk=order_id)
    return render(request, "orders/order/complete.html", context={"order": order})
