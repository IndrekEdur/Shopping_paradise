# Generated by Django 3.2.5 on 2021-11-28 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('budgets', '0006_alter_budget_item_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project'),
        ),
    ]
