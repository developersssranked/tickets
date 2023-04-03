from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
# Create your models here.

    

class Products(models.Model):
    start_punkt=models.CharField(verbose_name='Точка отправления',max_length=50)
    finish_punkt=models.CharField(verbose_name='Точка прибытия',max_length=50)
    price=models.PositiveIntegerField(verbose_name='Цена')
    quantity=models.IntegerField(verbose_name='Количество свободных мест',default=8)
    
    date=models.DateField(verbose_name='Дата поездки')
    time=models.TimeField(verbose_name='Время поездки')
    class Meta:                              #класс мета это создание доп настроек, с помощью этой мы сделали отображение в админке не POSTSS, а продукты, а также продукт в единственном числе
        verbose_name='Рейс'
        verbose_name_plural='Рейсы'

    weekday_choices = [
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье')
    ]
    weekday = models.CharField(verbose_name='День недели', null=True, max_length=10)
    
    def __str__(self):
        return f'{self.start_punkt+self.finish_punkt}'
@receiver(pre_save, sender=Products)
def calculate_weekday(sender, instance, **kwargs):
    instance.aboba=['Пн',"Вт","Ср","Чт","Пт","Сб","Вс"]
    instance.weekday = instance.aboba[instance.date.weekday()]
class Reserve(models.Model):
    name=models.CharField(verbose_name='Имя',max_length=30)
    surname=models.CharField(verbose_name='Фамилия',max_length=50)
    email=models.EmailField(verbose_name='Адрес электронной почты')
    is_paid=models.BooleanField(verbose_name='Оплачено ли',default=False)
    date_create=models.DateTimeField(verbose_name='Дата и время брони',auto_now_add=True)
    booking=models.ForeignKey(to=Products,verbose_name='Рейс',on_delete=models.CASCADE,null=True,blank=True)
   
    pets = models.BooleanField(
        verbose_name='Животные',default=False
    )
    phone_number=models.CharField(verbose_name='Номер телефона',max_length=20)
    bagage=models.BooleanField(verbose_name='Багаж',default=False)
    handbag=models.BooleanField(verbose_name='Ручная кладь',default=False)
    reserve_quantity=models.PositiveIntegerField(verbose_name='Количество забронированных мест')
    
    class Meta:                              #класс мета это создание доп настроек, с помощью этой мы сделали отображение в админке не POSTSS, а продукты, а также продукт в единственном числе
        verbose_name='Бронь'
        verbose_name_plural='Брони'
    def __str__(self):
        return f'Бронь на электронную почту {self.email} для {self.name} {self.surname}'