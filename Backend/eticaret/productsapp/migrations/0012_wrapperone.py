# Generated by Django 4.2 on 2023-06-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0011_urun_indirimli_fiyat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wrapperone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrapperResim1', models.ImageField(upload_to='wrapperphoto/')),
                ('wrapperResim2', models.ImageField(blank=True, null=True, upload_to='wrapperphoto/')),
                ('wrapperResim3', models.ImageField(blank=True, null=True, upload_to='wrapperphoto/')),
                ('wrapperResim4', models.ImageField(blank=True, null=True, upload_to='wrapperphoto/')),
                ('wrapperResim5', models.ImageField(blank=True, null=True, upload_to='wrapperphoto/')),
                ('wrapperText', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
