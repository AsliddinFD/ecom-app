# Generated by Django 4.2.1 on 2024-01-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_comments_comment_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.CharField(default='', max_length=255),
        ),
    ]
