# Generated by Django 4.1.6 on 2023-04-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateField(verbose_name='Дата поездки'),
        ),
    ]
