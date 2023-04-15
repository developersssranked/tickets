from django.db import models
from django.db.models.signals import pre_save,post_save,pre_delete
from django.dispatch import receiver

from datetime import timedelta
from django.utils import timezone
# Create your models here.
from telebot import TeleBot
from django.conf import settings
    

class Products(models.Model):
    punkt_choices=[
        ('Ist','Ist' ),
        ('Варна','Варна'),
        ('Бяла','Бяла'),
        ("Обзор","Обзор"),
        ("Святой влас","Святой влас"),
        ("Равда","Равда"),
        ("Солнечный берег","Солнечный берег"),
        ("Бургас","Бургас"),
        ]
    start_punkt=models.CharField(verbose_name='Точка отправления',max_length=50,choices=punkt_choices)
    finish_punkt=models.CharField(verbose_name='Точка прибытия',max_length=50,choices=punkt_choices)
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
        return f'Рейс {self.start_punkt}-{self.finish_punkt} Дата:{self.date} Время:{self.time} '
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
    telegram=models.BooleanField(verbose_name='Телеграм',default=True)
    
    
    class Meta:                              #класс мета это создание доп настроек, с помощью этой мы сделали отображение в админке не POSTSS, а продукты, а также продукт в единственном числе
        verbose_name='Бронь'
        verbose_name_plural='Брони'
    def __str__(self):
        return f'Бронь на электронную почту {self.email} для {self.name} {self.surname}'
    def auto_delete_order(self):
        
        if (self.is_paid==False) and ((timezone.now() - self.date_create).total_seconds() > 30):             #поменять на другое время автоудаление брони
                
                self.delete()
    def save(self, *args, **kwargs):
        bot_token = settings.TELEGRAM_BOT_API_KEY
        chat_id = '-912075038'
        bot = TeleBot(bot_token)
        message = f"Создана бронь на рейс {self.booking.start_punkt}-{self.booking.finish_punkt}. Оформлено билетов: {self.reserve_quantity}"
        bot.send_message(chat_id, message)
        super(Reserve, self).save(*args, **kwargs)
    
        
    
    

@receiver(pre_delete, sender=Reserve)
def update_related_model(sender, instance, **kwargs):
    related_model = instance.booking # получить связанный объект модели
    related_model.quantity += instance.reserve_quantity 
    related_model.save() # сохранить изменения

# @receiver(post_save, sender=Reserve)
# def order_post_save(sender, instance, **kwargs):
#     instance.send_message()
