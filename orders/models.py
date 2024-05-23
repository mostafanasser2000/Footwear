from django.db import models
from django.contrib.auth.models import User
from core.models import Product, ProductItem
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)

    # coupon = models.ForeignKey()
    # discount = models.SmallIntegerField(
    #     validators=[MinValueValidator(0), MaxValueValidator(100)]
    # )
    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    @property
    def subtotal(self):
        return self.total - self.get_discount()

    @property
    def total(self):
        return sum(item.total_cost for item in self.items.all())

    def get_discount(self):
        if self.discount:
            return self.total * (self.discount / Decimal(100))
        return Decimal(0)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.id)
