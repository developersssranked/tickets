from django.contrib import admin
from sales.models import Reserve,Products
# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=('start_punkt','finish_punkt','price','quantity','date','time')
    fields=('start_punkt','finish_punkt','price','quantity','date','time') #Создаем поля, которые будут отображаться в каждой записи. !Если создать внутри кортежа еще один кортеж, то значения, которые внутри подкортежа будут выводиться в одну строку.
    search_fields=('start_punkt',)           #Делаем поиск внутри админки(в кортеж передаем поле, по которому будем производить поиск)
            #Делаем сортировку по именам в алфавитном порядке
@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display=('name','surname','email','date_create','is_paid')
    fields=('name','surname','email','date_create','is_paid')
    search_fields=('email',)
    readonly_fields=('date_create',)
