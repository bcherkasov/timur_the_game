#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from notebook.services.config import ConfigManager
from IPython.display import clear_output
from random import randint, randrange, random
from datetime import date, datetime 
import pandas as pd
import time
import sys

cm = ConfigManager().update('notebook', {'limit_output': 0})

money = 100
food = 5
mood = 50
shit_counter = 1
day = 1

body = ['рука', 'жопа', 'печень', 'живот', 'нога', 'голова', 'двенадцатиперстная кишка', 'пизда', 'шея']

def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random() * 0.1 + 0.01)
    print('')


    
def wake_up(money, food, mood, shit_counter):
    
    work = ['Так, зубы почистил - красава..\nУмылся, побрился, - почти на человека стал похож!\nДавай теперь сижку ебни натощак!\nГондон конченый',
            'Опять сраная работа!\nКак же хочется, чтоб все отъебались!!!\nО, печенька\n*поднимает кусок печенья с грязного пола и с удовольствием съедает*',
            'О, здравствуй, солнышко!\nПривет, облачко!\nХорошего тебе дня, белочка!\nДобрый день, мне бутылку Жигулевского, пожалуйста',
            'Ща встану, резко соберусь и на работку дерну\nПо-бырому позиции напишу и можно будет за фенчиком поехать!\nЗаебись, идея!',
            'Пизда...\nНе надо было так накидываться вчера...\nЛучше бы пыхнул и спать завалился...\nОтче наш, ежи си на небеси...']
    
    shop = ['Ну наконец-то пойду пожру\nРабота заебала!!!\nКак круто было, когда на пароходики ходил хавать\nДаже коньячком иногда угощали!',
            'Может, пивасика еще цепануть заодно?\nДостали уже звонками с работы..\nКогда уже от меня все отстанут?\nО, чипсики по акции!',
            'Тааак, что у нас тут...\nМммм, котлетки с пюрешкой!\nПочти как в столовке на работе!\nЗаебииииись',
            'Да они охуели!\nКурица по 150 рублей!\nНадо было на работке пожрать...\nА бля, уже ведь не кормят...Пидоры',
            'Интересно, кто-нибудь заметит, если я пёрну по-тихоньку?\nВроде никто не заметил\nАхаха, лошары']
       
    weed = ['С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с неграми*\n*расстраивается из-за того, что своя елда не такая большая*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с чеченцами*\n*расстраивается, что в Таганроге нет овец*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с карликами*\n*расстраивается из-за того, что своя елда не такая большая*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с трансами*\n*расстраивается из-за того, что своя елда не такая большая*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с толстушками*\n*расстраивается из-за того, что Люба не такая большая*\n*разваливается на диване*']
    
    poop = ['Давай же, сука!!!\nВылазь, дерьмо, говнище! Блядь!\nКогда это я ел помидоры?',
            'Ну давай...\nродимая, давай...\nпожалуйста, вылазь, \nМРАЗЬ ТЫ ЕБАНАЯ СДОХНИ ТВАРЬ\nОхххх, вот это я понимаю кайф',
            'Хммм..\nВроде сегодня нормально выходит..\nНадо почаще насвай хавать!\nПойду Любе покажу, какие красивые ',
            'Получай, падла, теперь я знаю твою тайну!\nСраный демон!\nТебе осталось недолго\nПопрощайся со своими дружками!',
            'Хорошо иногда так вот посидеть одному и подумать.\nЯйца почесать.\nВ носу поковырять.\nМ! Вкусная козюля!']
    
    slowprint('Тимууууур..Тимууууур...ТИМУР!')
    slowprint('Ты спишь?')
    slowprint('Давай вставай, пидрила!')
    slowprint('Пора в порт пиздовать')
    print()
    
    a = input('[1] пойти на работу [2] сходить в магазин за едой [3] пыхнуть травки и подрочить [4] пойти посрать [5] что за нахуй здесь происходит?')
    print()
    
    if a == '1' and mood > 0:
        print('***Тимур сделал правильный выбор и решил заработать бабоса***')
        print()
        b = randint(0,4)
        slowprint(work[b])
        
        return 1
    
    elif a == '2' and money > 100:
        print('***Тимур решил не резать овцу, а купить еду как нормальные люди***')
        print()
        b = randint(0,4)
        slowprint(shop[b])
        
        return 2
        
    elif a == '3' and food > 1:
        print('***Тимур решил не напрягаться и предаться прелюбодеянию***')
        print()
        b = randint(0,4)
        slowprint(weed[b])
        
        return 3
        
    elif a == '4' and food > 2:
        print(f'***Тимур решил отомстить како-демону {shit_counter} уровня***')
        print()
        b = randint(0,4)
        slowprint(poop[b])
        
        return 4
    
    elif a == '5':
        
        return 5
    
    else:
        slowprint('Ну ты и дебиииил...День снова проебан зря!')
        
        return 0

    
def game():
   
    while shit_counter < 10:

        pain = body[randint(0,8)]

        slowprint(f'DAY {day}. У Тимура болит {pain}')
        print()
        print(f'### Зато {money} рублей в кармане!')
        print(f'### И много шашлыка! Аж {food}!')
        print(f'### Настроение так себе...на {mood} баллов по шкале Рейнхарта')
        print()
        activity = wake_up(money, food, mood, shit_counter)
        print()

        if activity == 1:

            new_money = randrange(50,250,20)
            money += new_money

            new_food = randint(1,2)
            food -= new_food

            if food < 0:
                food = 0

            new_mood = randrange(10,20,5)
            mood -= new_mood

            if mood < 0:
                mood = 0

            print()
            print(f'ИТОГИ {day} ДНЯ: +{new_money} рублей, -{new_food} шашлыка, -{new_mood} настроения по шкале Рейнхарта')
            day += 1
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')

        elif activity == 2:

            new_money = randrange(50,100,10)
            money -= new_money

            if money < 0:
                money = 0

            new_food = randint(1,4)
            food += new_food

            new_mood = randrange(10,20,5)
            mood -= new_mood

            if mood < 0:
                mood = 0

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_money} рублей, +{new_food} шашлыка, -{new_mood} настроения по шкале Рейнхарта')
            day += 1
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')


        elif activity == 3:

            new_money = randrange(10,50,10)
            money -= new_money

            if money < 0:
                money = 0

            new_food = randint(1,4)
            food -= new_food

            if food < 0:
                food = 0

            new_mood = randrange(5,30,5)
            mood += new_mood

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_money} рублей, -{new_food} шашлыка, +{new_mood} настроения по шкале Рейнхарта')
            day += 1
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')

        elif activity == 4:

            new_food = randint(1,4)
            food -= new_food

            if food < 0:
                food = 0

            shit_counter += 1

            new_mood = randrange(0,10,5)
            mood += new_mood

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_food} шашлыка, +{new_mood} настроения по шкале Рейнхарта')
            day += 1
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')

        elif activity == 5:

            slowprint("Ваше любопытство сослужило вам добрую службу!")
            print()
            slowprint('Данная программа была создана с целью вызвать экзистенциальный кризис у любого игрока. Это достигается путем симуляции жизни рядового морского агента.')
            slowprint('Задача состоит в том, чтобы найти в себе силы победить Властелина Преисподней путем дефекации.')
            slowprint('Для того, чтобы посрать, - нужна еда.')
            slowprint('Для того, чтобы купить еды, - нужны деньги.')
            slowprint('Для того, чтобы заработать денег, - нужно подходящее настроение.')
            slowprint('В общем, все как в жизни')
            slowprint('Разница лишь в том, что вы Тимур, а Тимур не вы, если вас действительно зовут Тимур')
            slowprint('Короче, одним словом, наслаждайтесь! Все права вроде бы защищены, но на всякий случай эта программа распространяется по лицензии WTFPL')
            slowprint('http://www.wtfpl.net/')
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')



        else:

            new_money = randrange(10,50,10)
            money -= new_money

            if money < 0:
                money = 0

            new_food = randint(1,2)
            food -= new_food

            if food < 0:
                food = 0

            new_mood = randrange(5,10,5)
            mood -= new_mood

            if mood < 0:
                mood = 0

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_money} рублей, -{new_food} шашлыка, -{new_mood} настроения по шкале Рейнхарта')
            day += 1
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')

        if money == 0 and food == 0 and mood == 0:
            print()
            print(f'ПИЗДА! Како-демон одержал победу на {day} день! Тимур сосет хуй!')
            print()
            print('  (\-"````"-/)')
            print('  //^\    /^\\\\')
            print(' ;/ ~_\  /_~ \;')
            print(' |  / \\\\// \  |')
            print('(,  \\0/  \\0/  ,)')
            print(' |   /    \   |')
            print(' | (_\.__./_) |')
            print('  \ \\v-..-v/ /')
            print('   \ `====\' /')
            print('    `\\\\\\///\'')
            print('       \/')
            time.sleep(10)
            break

        clear_output()