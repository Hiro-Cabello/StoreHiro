# Generated by Django 2.2.3 on 2022-07-17 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
            preserve_default=False,
        ),
    ]
