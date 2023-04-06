def date(dat):
                #заменяем все точки
    recycle = dat.maketrans('.', '-')
    recycle_date = dat.translate(recycle)
    print(recycle_date)

    sp_date = recycle_date.split('-')#делим по пробелу

    print(sp_date)
    if len(sp_date[2]) > 3 :  #переворачиваем если год не там где нужно
        sp_date = sp_date[::-1]
        print(sp_date)

    if len(sp_date[2]) == 1: #переделываем в 20023-01-06 , если пользователь написал 2023-1-6
        sp_date[2] = '0'+sp_date[2]

        print(sp_date)
        
    if len(sp_date[1]) == 1:
        sp_date[1] = '0'+sp_date[1]

        print(sp_date)


    date = sp_date[0]+ '-' + sp_date[1] + '-' + sp_date[2] #соеденяем
    print(date)
    date = date.replace(" ", "") #откудато могут взяться лишние пробелы, удаляем их
    print(date)
    
    return date


x = '8.04.2023'
print(date(x))