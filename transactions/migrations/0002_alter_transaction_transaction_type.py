# Generated by Django 4.2.7 on 2024-01-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan Paid'), (6, 'TRANSFER_OUT'), (5, 'TRANSFER_IN')], null=True),
        ),
    ]
