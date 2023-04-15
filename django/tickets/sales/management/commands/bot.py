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
    bot.send_message(
        help.chat.id ,
        'Приветствую, вы можете узнать кол-во свободных мест на тот или иной рейс, сформулировав такой запрос:\n@test_4524Bot место отправки, место прибытия, дата(гггг-мм-дд)\nпример записи:\n@test_4524Bot Солнечный берег, Бургас, 2023-09-05'
        )
    
    print(1)
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     if message == 'пр':
#         bot.message_handler(message.chat.id, 'все работает брат')

#     # while True:
#     #     x = 

    
        
# 	# bot.reply_to(message, message.text)

    

# @bot.message_handler(commands=['info'])
# def info(info):
#     while True:
#         first_bd = Products.objects.all()
#         sleep(10)
#         second_bd = Products.objects.all()
#         if len(first_bd) < len(second_bd):
#             bot.send_message(info.chat.id, 'прошли изменения')
#         else:
#             continue


@bot.message_handler (content_types =['text'])
def start (message):
    print(1)
    if '@test_4524Bot' in message.text:
        try:
            user = message.text
            lists = user.split(',')
            first_word = lists[0].split() #эта строчка отвечает за отделения пункта отправки от команды вызова бота
            lists[0] = first_word[1]
            # print(der_list)

            # достаем не обработанные слова
            fir_word_d = lists[0]
            sec_word_d = lists[1]
            thr_word_d = lists[2]
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

                sp_date = recycle_date.split('-')#делим по пробелу
                if len(sp_date[2]) > 3 :  #переворачиваем если год не там где нужно
                    sp_date = sp_date[::-1]

                if len(sp_date[2]) == 1: #переделываем в 20023-01-06 , если пользователь написал 2023-1-6
                    sp_date[2] = '0'+sp_date[2]
                    
                if len(sp_date[1]) == 1:
                    sp_date[1] = '0'+sp_date[1]


                date = sp_date[0]+ '-' + sp_date[1] + '-' + sp_date[2] #соеденяем
                date = date.replace(" ", "") #откудато могут взяться лишние пробелы, удаляем их
                
                return date
            
            # чистые слова
            start = recycle_w(fir_word_d)
            finish = recycle_w(sec_word_d)
            time= date(thr_word_d)
            

            

            filter_bd = Products.objects.filter(start_punkt = start, finish_punkt = finish, date = time) # достаем такой элемент из бд

            # bot.send_message(message.chat.id , f'{filter_bd}')
            # bot.send_message(message.chat.id , f'{start}, {finish}, {time}')

            if filter_bd.exists(): #проверяем есть ли такой элемент

                mesta = filter_bd.values_list('quantity') #достаем кол-во мест по ключу quantity

                # mesta1 = list(mesta[0])
                # mesta3 = mesta2[0]
                # mesta_finaly = list(mesta[0][0]) #обрабатыввем queryset превращая его в нормальную строку

                mesta_finaly = mesta[0][0]  #мистическое место, работало потом не работало, сейчас работает вот так
                
                bot.send_message(message.chat.id , f'по вашему запросу:\nместо отправки: {start}\nместо прибытия: {finish}\nдата: {time}\nсвободных мест на рейс: {mesta_finaly}') 



            else:  #если нету такого еэлемента
                bot.send_message(message.chat.id , f'не найденно таких поездок по вашему запросу\nместо отправки-{start}, место прибытия-{finish}, дата-{time}\nПопробуйте ввести данные еще раз. Пример запроса: @test_4524Bot Солнечный берег, Бургас, 2023-09-05')


        except Exception:
            print(Exception)
            bot.send_message(message.chat.id , f'Произошла ошибка при обработке ваших данных, проверьте их коректность.\nПример запроса: @test_4524Bot Солнечный берег, Бургас, 2023-09-05')