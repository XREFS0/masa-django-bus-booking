"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservationApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bus",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reservationApp.category",
            ),
        ),
    ]
