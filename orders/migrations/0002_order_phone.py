# Generated by Django 4.2.4 on 2024-05-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="phone",
            field=models.CharField(default="01111111111", max_length=15),
            preserve_default=False,
        ),
    ]
