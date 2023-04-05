from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from telebot import types
from time import sleep

from sales.models import Products


# Объявление переменной бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False) # пока что телеграм токен лежит в settings.py нужно добавить его в скрытый файл .env  и добавить его в гитигнор


# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()								# Загрузка обработчиков
        bot.infinity_polling()											# Бесконечный цикл бота

@bot.message_handler (commands= ["help"])
def help (help):
    bot.send_message(help.chat.id , 'приветствую, если вы хотите узнать о свободных местах на рейс, то упомяните меня в чате и напишите куда вы бы хотели поехать + дату "Варна, 13июня" ')
    bot.send_message(help.chat.id , f'{Products.objects.all()}')
    bot.send_message(help.chat.id , f'-------------')


    x = Products.objects.all()
    for cicle in x:
        name = cicle.start_punkt
        bot.send_message(help.chat.id , f'{name}')

    bot.send_message(help.chat.id , f'-------------------------------')

        
    bot.send_message(help.chat.id , f'{Products.objects.last()}')

    



'''
идеальный запрос :
бот Белорецк Учалы 2023-06-06
что может ввести пользователь:
1.бот белорецк учалы 2023-06-06  = все написанно с маленькой буквы
2.бот белорецку учады 2023-06-06 = написанно с маленькой ошибкой 
3.бот БЕЛОрецк УчаЛы 2023-06-06 = некоторые буквы написанны с большой 
4.бот 2023-06-06 Учалы Белорецк = написанно не в том порядке 
5.бот Белорецк, учалы, 2023-06-06 = написанно через запятые, дефисы и прочую хуйню 
6.

логика обработки :
1.деление:
1.1 
'''
@bot.message_handler (content_types =['text'])
def start (message):
    if '@test_4524Bot' in message.text:
        try:
            user = message.text
            list = user.split(',')
            first_word = list[0].split() #эта строчка отвечает за отделения пункта отправки от команды вызова бота
            list[0] = first_word[1]
            # print(der_list)

            # достаем не обработанные слова
            fir_word_d = list[0]
            sec_word_d = list[1]
            thr_word_d = list[2]
            # print ( fir_word_d, sec_word_d , thr_word_d)


            #обрабатываем слова 
            def recycle_w (word):
                if 'I' in word or 'i' in word or 'S' in word or 's' in word :
                    clear_w = 'IST'
                    return clear_w 

                if 'Ва' in word or 'ва' in word or 'арн' in word or 'ве' in word:
                    clear_w = 'Варна'
                    return clear_w
                if 'Бя' in word or 'бя' in word or 'яла' in word:
                    clear_w = 'Бяла'
                    return clear_w
                if 'Об' in word or 'об' in word or 'зор' in word:
                    clear_w = 'Обзор'
                    return clear_w
                if 'Свя' in word or 'свя' in word or 'Вла' in word or 'вла' in word:
                    clear_w = 'Святой Влас'
                    return clear_w
                if 'Ра' in word or 'ра' in word or 'вда' in word:
                    clear_w = 'Равда'
                    return clear_w
                if 'Сол' in word or 'сол' in word or 'бер' in word or 'нечн' in word:
                    clear_w = 'Солнечный берег'
                    return clear_w
                if 'Бур' in word or 'бур' in word or 'гас' in word:
                    clear_w = 'Бургас'
                    return clear_w


            # год-месяц-день
            # 2023-04-04 обработка даты 
        
            def date(dat):
                #заменяем все точки
                recycle = dat.maketrans('.', '-')
                recycle_date = dat.translate(recycle)

                sp_date = recycle_date.split('-')
                if len(sp_date[2]) > 3 :
                    sp_date = sp_date[::-1]



                date = sp_date[0]+ '-' + sp_date[1] + '-' + sp_date[2]
                date = date.replace(" ", "")
                
                return date

    



            # чистые слова
            start = recycle_w(fir_word_d)
            finish = recycle_w(sec_word_d)
            time= date(thr_word_d)

            # bot.send_message(message.chat.id , f'{start}')
            # bot.send_message(message.chat.id , f'{finish}')
            # bot.send_message(message.chat.id , f'{time}')

            


        
        except Exception :
            print(Exception)
            # введите коректный запрос






#1. выводить инструкцию правильного запроса 
#2.принимать текст пользователя 
# 3. определять валидный ли он
# 3.1 откуда - for products.start_punkt
# 3.2 куда - for prod.finish_punkt
# 3.3 дата -for products.data\
# сравнение полученных данных с бд
# вывод - свободные места prod.quantity

# 4. делить его на состовляющие (куда, дата)
# 5. проверять через цикл по бузе данных "пункт назначения" по числу
# 6. брать из бд и выводить количество свободных мест, вместе с сылкой на бронировние
    

# если кто то забронировал билет бот должен отправлять анонимно куда его забронировали ()


