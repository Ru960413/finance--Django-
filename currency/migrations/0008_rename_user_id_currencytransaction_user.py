# Generated by Django 4.1.1 on 2023-04-14 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_currencytransaction_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currencytransaction',
            old_name='user_id',
            new_name='user',
        ),
    ]
