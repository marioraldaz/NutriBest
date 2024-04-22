# Generated by Django 4.2.1 on 2024-04-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0003_alter_ingredient_spoonacular_id_and_more"),
        ("profiles", "0003_alter_userprofile_saved_recipes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="saved_recipes",
            field=models.ManyToManyField(
                blank=True, related_name="saved_by_profiles", to="foods.recipe"
            ),
        ),
    ]
