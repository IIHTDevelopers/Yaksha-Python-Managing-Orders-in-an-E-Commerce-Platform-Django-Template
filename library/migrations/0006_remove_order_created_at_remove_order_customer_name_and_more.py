# Generated by Django 4.2.19 on 2025-03-14 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0005_order_delete_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="order",
            name="customer_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="order_number",
        ),
        migrations.RemoveField(
            model_name="order",
            name="status",
        ),
        migrations.RemoveField(
            model_name="order",
            name="total_price",
        ),
    ]
