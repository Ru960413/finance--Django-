# Generated by Django 4.1.1 on 2023-03-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='interest',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
