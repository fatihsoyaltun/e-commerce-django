# Generated by Django 4.1.7 on 2023-08-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_myuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, default='Belirtilmemiş', max_length=100, null=True),
        ),
    ]
