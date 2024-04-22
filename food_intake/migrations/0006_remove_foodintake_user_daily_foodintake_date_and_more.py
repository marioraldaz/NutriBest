# Generated by Django 5.0.2 on 2024-04-17 17:42

import datetime
import django.db.models.deletion
import utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food_intake", "0005_alter_foodintake_meal_type"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="foodintake",
            name="user_daily",
        ),
        migrations.AddField(
            model_name="foodintake",
            name="date",
            field=models.DateField(
                default=datetime.date(2024, 1, 1),
                validators=[utils.validators.validate_meal_type],
            ),
        ),
        migrations.AddField(
            model_name="userdaily",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="profiles.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="foodintake",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="profiles.userprofile",
            ),
        ),
    ]