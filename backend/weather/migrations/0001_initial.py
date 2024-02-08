# Generated by Django 5.0.2 on 2024-02-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=127)),
                ("lat", models.FloatField()),
                ("lon", models.FloatField()),
                ("last_fetch_time", models.DateTimeField(null=True)),
                ("temp", models.IntegerField(null=True)),
                ("pressure", models.IntegerField(null=True)),
                ("wind_speed", models.IntegerField(null=True)),
            ],
        ),
    ]