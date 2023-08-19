# Generated by Django 4.1.7 on 2023-08-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_profile_balance"),
    ]

    operations = [
        migrations.CreateModel(
            name="History",
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
                ("Sender", models.CharField(default="", max_length=100)),
                ("Reciver", models.CharField(default="", max_length=100)),
                (
                    "Money",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="profile",
            name="balance",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]
