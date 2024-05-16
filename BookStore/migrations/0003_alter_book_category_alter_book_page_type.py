# Generated by Django 5.0.6 on 2024-05-16 00:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BookStore", "0002_alter_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.CharField(
                choices=[
                    ("Romance", "ROMANCE"),
                    ("Thriller", "THRILLER"),
                    ("Biography", "BIOGRAPHY"),
                    ("Classic", "CLASSIC"),
                    ("Drama", "DRAMA"),
                    ("History", "HISTORY"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="page_type",
            field=models.CharField(
                choices=[("Hard", "HARD"), ("Soft", "SOFT")], max_length=20
            ),
        ),
    ]