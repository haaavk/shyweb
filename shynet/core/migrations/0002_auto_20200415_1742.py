# Generated by Django 3.0.5 on 2020-04-15 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="service", options={"ordering": ["name", "uuid"]},
        ),
    ]