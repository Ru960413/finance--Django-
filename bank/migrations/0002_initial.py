# Generated by Django 4.1.1 on 2023-03-27 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.bankaccount'),
        ),
    ]
