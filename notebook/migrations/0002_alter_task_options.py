# Generated by Django 4.2.6 on 2023-10-31 12:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notebook", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("is_done", "created")},
        ),
    ]
