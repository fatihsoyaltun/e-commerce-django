# Generated by Django 4.1.7 on 2023-06-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0006_alter_urun_kategori_alter_urun_urunresmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='fiyat',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]