# Generated by Django 4.1.1 on 2023-04-14 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_rename_account_id_currencytransaction_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currencytransaction',
            old_name='account',
            new_name='account_id',
        ),
    ]
