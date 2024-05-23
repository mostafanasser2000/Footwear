from cart.models import Cart

def cart(request):
    return {'cart': Cart.objects.get(user=request.user)}