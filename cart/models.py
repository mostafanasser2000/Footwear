from django.db import models
from django.contrib.auth.models import User
from core.models import ProductItem

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, related_name="cart", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} Cart"

    @property
    def subtotal(self):
        return sum([item.price for item in self.items.all()])

class CartItem(models.Model):
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")

    class Meta:
        unique_together = ("cart", "item")

    def save(self, *args, **kwargs):
        self.unit_price = self.item.product.price
        self.price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item.product.name
