# Generated by Django 4.2 on 2023-07-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0019_alter_sepet_toplam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepet',
            name='toplam',
            field=models.IntegerField(null=True),
        ),
    ]
