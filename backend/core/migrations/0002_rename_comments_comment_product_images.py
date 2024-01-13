# Generated by Django 4.2.1 on 2024-01-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
