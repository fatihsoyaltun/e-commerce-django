# Generated by Django 4.2.3 on 2023-07-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0024_alter_sepet_toplam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepet',
            name='toplam',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
