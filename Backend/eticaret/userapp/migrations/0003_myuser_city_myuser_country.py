# Generated by Django 4.1.7 on 2023-07-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_myuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
