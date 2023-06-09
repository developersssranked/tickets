# Generated by Django 4.1.6 on 2023-04-15 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_punkt', models.CharField(choices=[('Ist', 'Ist'), ('Варна', 'Варна'), ('Бяла', 'Бяла'), ('Обзор', 'Обзор'), ('Святой влас', 'Святой влас'), ('Равда', 'Равда'), ('Солнечный берег', 'Солнечный берег'), ('Бургас', 'Бургас')], max_length=50, verbose_name='Точка отправления')),
                ('finish_punkt', models.CharField(choices=[('Ist', 'Ist'), ('Варна', 'Варна'), ('Бяла', 'Бяла'), ('Обзор', 'Обзор'), ('Святой влас', 'Святой влас'), ('Равда', 'Равда'), ('Солнечный берег', 'Солнечный берег'), ('Бургас', 'Бургас')], max_length=50, verbose_name='Точка прибытия')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('quantity', models.IntegerField(default=8, verbose_name='Количество свободных мест')),
                ('date', models.DateField(verbose_name='Дата поездки')),
                ('time', models.TimeField(verbose_name='Время поездки')),
                ('weekday', models.CharField(max_length=10, null=True, verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачено ли')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время брони')),
                ('pets', models.BooleanField(default=False, verbose_name='Животные')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('bagage', models.BooleanField(default=False, verbose_name='Багаж')),
                ('handbag', models.BooleanField(default=False, verbose_name='Ручная кладь')),
                ('reserve_quantity', models.PositiveIntegerField(verbose_name='Количество забронированных мест')),
                ('telegram', models.BooleanField(default=True, verbose_name='Телеграм')),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.products', verbose_name='Рейс')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
    ]
