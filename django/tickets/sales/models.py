from django.db import models

# Create your models here.

    

class Products(models.Model):
    start_punkt=models.CharField(verbose_name='Точка отправления',max_length=50)
    finish_punkt=models.CharField(verbose_name='Точка прибытия',max_length=50)
    price=models.PositiveIntegerField(verbose_name='Цена')
    quantity=models.IntegerField(verbose_name='Количество свободных мест',default=8)
    
    date=models.DateTimeField(verbose_name='Дата и время поездки')
    class Meta:                              #класс мета это создание доп настроек, с помощью этой мы сделали отображение в админке не POSTSS, а продукты, а также продукт в единственном числе
        verbose_name='Рейс'
        verbose_name_plural='Рейсы'
    def __str__(self):
        return f'{self.start_punkt+self.finish_punkt}'
class Reserve(models.Model):
    name=models.CharField(verbose_name='Имя',max_length=30)
    surname=models.CharField(verbose_name='Фамилия',max_length=50)
    email=models.EmailField(verbose_name='Адрес электронной почты')
    is_paid=models.BooleanField(verbose_name='Оплачено ли',default=False)
    date_create=models.DateTimeField(verbose_name='Дата и время брони',auto_now_add=True)
    booking=models.ForeignKey(to=Products,verbose_name='Рейс',on_delete=models.CASCADE,null=True,blank=True)
    pets=models.BooleanField(verbose_name='Животные')
    
    class Meta:                              #класс мета это создание доп настроек, с помощью этой мы сделали отображение в админке не POSTSS, а продукты, а также продукт в единственном числе
        verbose_name='Бронь'
        verbose_name_plural='Брони'
    def __str__(self):
        return f'Бронь на электронную почту {self.email} для {self.name} {self.surname}'