from cart.models import Cart


def cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return {"cart": cart}
    else:
        return {"cart": None}
