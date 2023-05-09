# Generated by Django 4.1.7 on 2023-05-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_alter_order_food_preference"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone_no", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=200)),
                ("landmark", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("pincode", models.CharField(max_length=10)),
                ("food_type", models.CharField(max_length=10)),
                ("fresh_food_available", models.BooleanField(default=False)),
                ("food_remains_available", models.BooleanField(default=False)),
                ("fresh_food_capacity", models.IntegerField(default=0)),
                ("food_remains_capacity", models.IntegerField(default=0)),
                ("description", models.TextField(blank=True)),
            ],
        ),
    ]
