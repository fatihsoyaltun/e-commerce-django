# Generated by Django 4.1.7 on 2023-08-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_alter_myuser_address_alter_myuser_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.TextField(blank=True, default='', max_length=250, null=True),
        ),
    ]
