# Generated by Django 4.2.3 on 2023-08-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0038_remove_kurulum_kurulumresim_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurulum',
            name='videoBaslik',
        ),
    ]
