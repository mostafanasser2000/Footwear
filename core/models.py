from django.db import models
from django.utils.text import slugify
from PIL import Image
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "brand"
        verbose_name_plural = "brands"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ("name",)
        verbose_name = "color"
        verbose_name_plural = "colors"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ("name",)
        verbose_name = "size"
        verbose_name_plural = "sizes"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Gender(models.TextChoices):
        MEN = "men", "Men"
        WOMEN = "women", "Women"
        BOTH = "both", "Both"

    category = models.ForeignKey(
        "Category", related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    gender = models.CharField(
        max_length=10, choices=Gender.choices, default=Gender.BOTH
    )
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:product_detail", kwargs={"slug": self.slug, "id": self.id})

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    size = models.ForeignKey(Size, related_name="items", on_delete=models.CASCADE)
    color = models.ForeignKey(Color, related_name="items", on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product} - {self.size} - {self.color}"
