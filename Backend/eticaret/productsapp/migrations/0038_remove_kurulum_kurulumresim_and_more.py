# Generated by Django 4.2.3 on 2023-08-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0037_kurulum_kurulumresim2_kurulum_kurulumresim3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurulum',
            name='kurulumResim',
        ),
        migrations.RemoveField(
            model_name='kurulum',
            name='kurulumResim2',
        ),
        migrations.RemoveField(
            model_name='kurulum',
            name='kurulumResim3',
        ),
        migrations.RemoveField(
            model_name='kurulum',
            name='kurulumResim4',
        ),
        migrations.RemoveField(
            model_name='kurulum',
            name='kurulumResim5',
        ),
        migrations.RemoveField(
            model_name='kurulum',
            name='kurulumResim6',
        ),
    ]
