# Generated by Django 5.1.5 on 2025-02-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("discription", models.CharField(max_length=100)),
                ("image", models.ImageField(default="", upload_to="media/image")),
                ("price", models.IntegerField(default=0)),
                ("hire_date", models.DateField()),
            ],
        ),
    ]
