# Generated by Django 4.2.6 on 2023-10-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.TextField()),
                ("created", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("is_done", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(related_name="tasks", to="notebook.tag"),
                ),
            ],
            options={
                "ordering": ("created", "is_done"),
            },
        ),
    ]
