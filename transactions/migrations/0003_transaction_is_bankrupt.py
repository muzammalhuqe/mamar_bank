# Generated by Django 4.2.7 on 2024-01-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]