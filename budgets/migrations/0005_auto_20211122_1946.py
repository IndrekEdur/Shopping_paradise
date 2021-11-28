# Generated by Django 3.2.5 on 2021-11-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0004_auto_20211122_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_item',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
        ),
        migrations.AlterField(
            model_name='budget_item',
            name='product_quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
        ),
    ]