# Generated by Django 5.1 on 2024-10-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_no',
            field=models.PositiveBigIntegerField(null=True, unique=True),
        ),
    ]