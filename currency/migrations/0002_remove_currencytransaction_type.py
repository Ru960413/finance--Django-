# Generated by Django 4.1.1 on 2023-04-11 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencytransaction',
            name='type',
        ),
    ]