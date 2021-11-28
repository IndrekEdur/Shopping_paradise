# Generated by Django 3.2.5 on 2021-11-27 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='products'),
            preserve_default=False,
        ),
    ]