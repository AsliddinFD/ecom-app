# Generated by Django 4.2.1 on 2024-01-10 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 7, 17, 32, 160483, tzinfo=datetime.timezone.utc)),
        ),
    ]
