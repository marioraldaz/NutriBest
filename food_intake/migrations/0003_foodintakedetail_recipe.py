# Generated by Django 5.0.3 on 2024-05-07 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food_intake", "0002_remove_foodintakedetail_recipe"),
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodintakedetail",
            name="recipe",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="foods.recipe",
            ),
            preserve_default=False,
        ),
    ]
