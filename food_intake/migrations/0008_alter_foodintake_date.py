# Generated by Django 5.0.2 on 2024-04-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food_intake", "0007_alter_foodintake_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodintake",
            name="date",
            field=models.DateField(),
        ),
    ]