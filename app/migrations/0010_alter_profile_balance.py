# Generated by Django 4.1.7 on 2023-08-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_profile_id_alter_profile_mobile_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="balance",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]