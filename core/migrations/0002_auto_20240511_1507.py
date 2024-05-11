from django.db import migrations
from core.models import Category, Brand, Size, Color


def create_initial_data(apps, schema_editor):
    Category.objects.create(name="Sports")
    Category.objects.create(name="Dress")
    Category.objects.create(name="Casuals")

    brands = [
        "Addidas",
        "Nike",
        "Puma",
        "GUCCI",
        "Reebok",
        "New Balance",
        "Vans",
    ]
    for brand in brands:
        Brand.objects.create(name=brand)

    sizes = [
        "7",
        "7.5",
        "8",
        "8.5",
        "9",
        "9.5",
        "10",
        "10.5",
        "11",
        "11.5",
        "12",
        "12.5",
        "13",
        "13.5",
        "14",
    ]
    
    for size in sizes:
        Size.objects.create(name=size)
    
    colors = [
        "Black",
        "White",
        "Blue",
        "Red",
        "Green",
        "Grey",
        "Orange",
        "Cream",
        "Brown"
    ]
    
    for color in colors:
        Color.objects.create(name=color)


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = []
