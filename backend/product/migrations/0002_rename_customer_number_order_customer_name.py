# Generated by Django 5.0.4 on 2024-05-05 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_number',
            new_name='customer_name',
        ),
    ]
