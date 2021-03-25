from notebook.services.config import ConfigManager
from IPython.display import clear_output
from random import randint, randrange, random
from datetime import date, datetime 
import time
import sys

cm = ConfigManager().update('notebook', {'limit_output': 0})

money = 100
food = 5
mood = 50
shit_counter = 1
day = 1

body = ['рука', 'жопа', 'печень', 'живот', 'нога', 'голова', 'двенадцатиперстная кишка', 'пизда', 'шея']

my_hero = {'name': 'Тимур',
           'race': 'лезгин',
           'class': 'варвар',
           'attack': 10,
           'def': 8,
           'hp': 100}

villain = {'name': 'Баал-Зебуб',
         'race': 'демон',
         'class': 'туалетный',
         'attack': 15,
         'def': 10,
         'hp': 300}

quest1 = {'quest': 'Как расшифровывается аббревиатура FDEDANRSAOCLONL?',
          'answ1': 'Freight Dreamed Easy Doing Anything Non-Restrictive Sound And Or Capable Loading Or Not Loading',
          'answ2': 'Freight Damned Earned, Discharging And Non-Reloaded Ship And Or Cargo Lost Or Not Lost',
          'answ3': 'Freight Deemed Earned, Discountless And Non-Returnable Ship And Or Cargo Lost Or Not Lost',
          'correct': 3}

quest2 = {'quest': 'Что означает фраза 1 SPSB AAAA?',
          'answ1': '1 Safe Port Safe Berth Always Available Always Afloat',
          'answ2': '1 Scary Policeman Sexy Bitch Always Asphixiates Always Alive',
          'answ3': '1 Sativa Produces Smoke But Always And Alas Always',
          'correct': 1}

quest3 = {'quest': 'Сколько часов сталии у судна, погрузившего 3500 т при норме 1000 MTS PER WWD?',
          'answ1': '72 часа',
          'answ2': '80 часов',
          'answ3': '84 часа',
          'correct': 3}

quest4 = {'quest': 'Что означает STEM?',
          'answ1': 'Subject To Enough Millets',
          'answ2': 'Subject To Enough Merchandise',
          'answ3': 'Subject To Enough Moisture',
          'correct': 2}

quest5 = {'quest': 'Какой интейк у панамакса?',
          'answ1': '10\'000-20\'000 тон',
          'answ2': '50\'000-120\'000 тон',
          'answ3': '60\'000-180\'000 тон',
          'correct': 2}

quest6 = {'quest': 'Какая чартер-партия лучше заточена под фрахтователя?',
          'answ1': 'NorGrain',
          'answ2': 'GenCon',
          'answ3': 'Synacomex',
          'correct': 3}

quest7 = {'quest': 'Какая чартер-партия лучше заточена под судовладельца?',
          'answ1': 'NorGrain',
          'answ2': 'GenCon',
          'answ3': 'Synacomex',
          'correct': 2}

quest8 = {'quest': 'Имеет ли право фрахтователь, подписавший чартер-партию Synacomex, отказаться принимать судно, опоздавшее в свой лейкен?',
          'answ1': 'Да',
          'answ2': 'Нет',
          'answ3': 'У меня есть пупок',
          'correct': 1}

action_quests = [quest1, quest2, quest3, quest4]
story_quests = [quest5, quest6, quest8, quest7]

def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random() * 0.1 + 0.01)
    print('')
    


def fight_with_demon():
    
    for i in range(50):
    
        a = randint(1,20)
        b = randint(1,20)
        
        hero_name = my_hero['name'] + ', ' + my_hero['class'] + ' ' + my_hero['race']
        hero_def = my_hero['def']
        hero_hp = my_hero['hp']
        hero_attack = my_hero['attack'] + a
        villain_name = villain['name'] + ', ' + villain['class'] + ' ' + villain['race']
        villain_hp = villain['hp']
        villain_attack = villain['attack'] + b
        
        if i > 0 and i % 5 == 0:
            
            try:
                index = int(i/5-1)
                quiz = action_quests[index]['quest']
                slowprint('Неожиданно Тимур получает сообщение от Иващенко:')
                print()
                slowprint('- Проститутки! Пидорасы!')
                slowprint(quiz)
                print()
                print('[1] ' + action_quests[index]['answ1'])
                print('[2] ' + action_quests[index]['answ2'])
                print('[3] ' + action_quests[index]['answ3'])
                answer = input()
                
                if int(answer) == action_quests[index]['correct']:
                    print()
                    slowprint('Како-демон охуел от такой эрудированности Тимура и открылся для неожиданного удара!')
                    hero_attack = my_hero['attack'] + a
                    
                    if hero_attack > villain['def']:
                        
                        villain_hp -= (hero_attack - villain['def'])

                        if villain_hp > 0:
                            slowprint(f'Бедный {villain_name}! \nТеперь у него всего {villain_hp} хп')
                            villain['hp'] = villain_hp
                            input()
                        else:
                            slowprint(f'ДА!!!! Тимур победил {villain_name}! \nТеперь он не сможет никого хватать за яйца!')
                            input()
                            return 1
                            break
                    else:
                        slowprint(f'{villain_name}, парировал твой удар, {hero_name}!')
                        
                else:
                    print()
                    slowprint('Како-демон посмеялся над тупостью Тимура и предложил ему пойти нахуй!')
                    print()
                    
                
            except IndexError:
                pass
            
            
        print()
        print(f'ROUND {i+1}')
        action = input('Выбери действие: [1] атака [2] защита [3] пыхнуть напас')
        print()

        if action == '1':

            slowprint(f'Тимур ебашит на {hero_attack} урона!')
            if hero_attack > villain['def']:
                villain_hp -= (hero_attack - villain['def'])

                if villain_hp > 0:
                    slowprint(f'Бедный {villain_name}! \nТеперь у него всего {villain_hp} хп')
                    villain['hp'] = villain_hp
                    input()
                else:
                    slowprint(f'ДА!!!! Тимур победил {villain_name}! \nТеперь он не сможет никого хватать за яйца!')
                    input()
                    return 1
                    break

                
                slowprint(f'{villain_name}, гасит вас на {villain_attack} урона!')

                if villain_attack > hero_def:
            
                    hero_hp -= (villain_attack - hero_def)
                    my_hero['hp'] = hero_hp
                    
                    slowprint(f'{villain_name}, херачит на {villain_attack} урона!')

                    if hero_hp > 0:
                        slowprint(f'{villain_name}, нормально так навалял Тимуру! \nОсталось {hero_hp} хп')
                        input()
                    else:
                        slowprint(f'{villain_name}, завалил тебя, {hero_name}! \nТеперь для тебя вероятность потрахаться равна 0%!')
                        input()
                        return 0
                        break

                else:
                    slowprint(f'{hero_name}, отбил удар {villain_name}!')
                    input()
                
                
            else:
                slowprint(f'{villain_name}, парировал твой удар, {hero_name}!')
                print()
                slowprint(f'{villain_name}, гасит вас на {villain_attack} урона!')

                if villain_attack > hero_def:
            
                    hero_hp -= (villain_attack - hero_def)
                    my_hero['hp'] = hero_hp
                    
                    slowprint(f'{villain_name}, херачит на {villain_attack} урона!')

                    if hero_hp > 0:
                        slowprint(f'{villain_name}, нормально так навалял Тимуру! \nОсталось {hero_hp} хп')
                        input()
                    else:
                        slowprint(f'{villain_name}, завалил тебя, {hero_name}! \nТеперь для тебя вероятность потрахаться равна 0%!')
                        input()
                        return 0
                        break
                        
                else:
                    slowprint(f'{hero_name}, отбил удар {villain_name}!')
                    input()
                    
            print()

        elif action == '2':

            a = randint(1,20)
            b = randint(1,20)

            my_hero['def'] += a
            slowprint(f'Тимур чувствует себя в {a} раз защищеннее! Никакая напасть ему не страшна с презервативами Contex!')
            input('Пизданись головой об клаву, чтобы продолжить...')

            if villain_attack > hero_def:
            
                hero_hp -= (villain_attack - hero_def)
                my_hero['hp'] = hero_hp
                
                slowprint(f'{villain_name}, херачит на {villain_attack} урона!')

                if hero_hp > 0:
                    slowprint(f'{villain_name}, нормально так навалял Тимуру! \nОсталось {hero_hp} хп')
                    input()
                else:
                    slowprint(f'{villain_name}, завалил тебя, {hero_name}! \nТеперь для тебя вероятность потрахаться равна 0%!')
                    input()
                    return 0
                    break
            
            else:
                slowprint(f'{hero_name}, отбил удар {villain_name}!')
                input()

            my_hero['def'] = 10
            print()
            
        else:
            
            slowprint('Тимур достал косяк, прикурил и предложил затянуться како-демону!')
            slowprint('Тот отказался, что придало Тимуру уверенности в своих силах!')
            a = randint(1,20)
            b = randint(1,10)
            
            my_hero['def'] += a
            my_hero['attack'] +=b
            hero_def = my_hero['def']
            slowprint(f'Защита Тимура увеличилась на {a}! Атака Тимура увеличилась на {b}!')
            print()
            
            if villain_attack > hero_def:
            
                hero_hp -= (villain_attack - hero_def)
                my_hero['hp'] = hero_hp
                
                slowprint(f'{villain_name}, херачит на {villain_attack} урона!')

                if hero_hp > 0:
                    slowprint(f'{villain_name}, нормально так навалял Тимуру! \nУ него осталось {hero_hp} хп')
                    input()
                else:
                    slowprint(f'{villain_name}, завалил тебя, {hero_name}! \nТеперь для тебя вероятность потрахаться равна 0%!')
                    input()
                    return 0
                    break
            
            else:
                slowprint(f'{hero_name}, отбил удар {villain_name}!')
        
        print()

  
    
def wake_up(money, food, mood, shit_counter):
    
    work = ['Так, зубы почистил - красава..\nУмылся, побрился, - почти на человека стал похож!\nЩа сижку ебну натощак и вообще заебись будет!\nБля, как же низко я пал...',
            'Опять сраная работа!\nКак же хочется, чтоб все отъебались!!!\nО, печенька\n*поднимает кусок печенья с грязного пола и с удовольствием съедает*',
            'О, здравствуй, солнышко!\nПривет, облачко!\nХорошего тебе дня, белочка!\nДобрый день, мне бутылочку Жигулевского, пожалуйста',
            'Ща встану, резко соберусь и на работку дерну\nПо-бырому позиции напишу и можно будет за фенчиком поехать!\nЗаебись, идея!',
            'Пизда...\nНе надо было так накидываться вчера...\nЛучше бы пыхнул и спать завалился...\nОтче наш, ежи си на небеси...']
    
    shop = ['Ну наконец-то пойду пожру\nРабота заебала!!!\nКак круто было, когда на пароходики ходил хавать\nДаже коньячком иногда угощали!',
            'Может, пивасика еще цепануть заодно?\nДостали уже звонками с работы..\nКогда уже от меня все отстанут?\nО, чипсики по акции!',
            'Тааак, что у нас тут...\nМммм, котлетки с пюрешкой!\nПочти как в столовке на работе!\nЗаебииииись',
            'Да они охуели!\nКурица по 150 рублей!\nНадо было на работке пожрать...\nА бля, уже ведь не кормят...Пидоры',
            'Интересно, кто-нибудь заметит, если я пёрну потихоньку?\nВроде никто не заметил\nАхаха, лошары']
       
    weed = ['С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с неграми*\n*расстраивается из-за того, что своя елда не такая большая*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с чеченцами*\n*расстраивается, что в Таганроге нет овец*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с карликами*\n*расстраивается из-за того, что своя елда не такая большая*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с трансами*\n*расстраивается из-за того, что своя елда не такая большая*\n*разваливается на диване*',
            'С другой стороны сегодня можно и почилить\n*достает пакет травки и раздувается*\n*включает порно с толстушками*\n*расстраивается из-за того, что Люба не такая большая*\n*разваливается на диване*']
    
    poop = ['Давай же, сука!!!\nВылазь, дерьмо, говнище! Блядь!\nКогда это я ел помидоры?',
            'Ну давай...\nродимая, давай...\nпожалуйста, вылазь, \nМРАЗЬ ТЫ ЕБАНАЯ СДОХНИ ТВАРЬ\nОхххх, вот это я понимаю кайф',
            'Хммм..\nВроде сегодня нормально выходит..\nНадо почаще насвай хавать!\nПойду Любе покажу, какие красивые ',
            'Получай, падла, теперь я знаю твою тайну!\nСраный демон!\nТебе осталось недолго\nПопрощайся со своими дружками!',
            'Хорошо иногда так вот посидеть одному и подумать.\nЯйца почесать.\nВ носу поковырять.\nСука! Опять туалетная бумага закончилась!!!']
    
    slowprint('Тимууууур..Тимууууур...ТИМУР!')
    slowprint('Ты спишь?')
    slowprint('Давай вставай, пидрила!')
    slowprint('Пора в порт пиздовать')
    print()
    print('[1] пойти на работу')
    print('[2] сходить в магазин за едой')
    print('[3] пыхнуть травки и подрочить')
    print('[4] пойти посрать')
    print('[5] что за нахуй здесь происходит?')
    
    a = input()
    print()
    
    if a == '1' and mood >= 10:
        print('***Тимур сделал правильный выбор и решил заработать бабоса***')
        print()
        b = randint(0,4)
        slowprint(work[b])
        
        return 1
    
    elif a == '2' and money > 100:
        print('***Тимур решил не резать барана, а купить еду как нормальные люди***')
        print()
        b = randint(0,4)
        slowprint(shop[b])
        
        if b == 1 or b == 2 or b == 4:
            return 6
        else:
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
    
    money = 100
    food = 5
    mood = 50
    shit_counter = 1
    day = 1
   
    while shit_counter < 10:

        pain = body[randint(0,8)]

        slowprint(f'DAY {day}. У Тимура болит {pain}')
        print()
        if money > 0:
            print(f'### Зато {money} рублей в кармане!')
        else:
            print(f'### И к тому же жопа с деньгами!')
        if food > 0:
            print(f'### А как много шашлыка! Ммммм...аж {food}!')
        else:
            print('### Да и хавки совсем не осталось...')    
        if mood > 0:
            print(f'### Настроение так себе...на {mood} баллов по шкале Шишкаридзе')
        else:
            print(f'### Настроение ни к черту... Даже Шишкаридзе охуел!')
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
            print(f'ИТОГИ {day} ДНЯ: +{new_money} рублей, -{new_food} шашлыка, -{new_mood} настроения по шкале Шишкаридзе')
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
            print(f'ИТОГИ {day} ДНЯ: -{new_money} рублей, +{new_food} шашлыка, -{new_mood} настроения по шкале Шишкаридзе')
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

            new_mood = randrange(15,30,5)
            mood += new_mood

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_money} рублей, -{new_food} шашлыка, +{new_mood} настроения по шкале Шишкаридзе')
            day += 1
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')

        elif activity == 4:

            new_food = randint(1,4)
            food -= new_food

            if food < 0:
                food = 0

            shit_counter += 1

            new_mood = randrange(0,5,5)
            mood += new_mood

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_food} шашлыка, +{new_mood} настроения по шкале Шишкаридзе')
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
            slowprint('В общем, все как в жизни.')
            slowprint('Разница лишь в том, что вы Тимур, а Тимур не вы, если вас действительно зовут Тимур.')
            slowprint('Короче, одним словом, наслаждайтесь! Все права вроде бы защищены, но на всякий случай эта программа распространяется по лицензии WTFPL:')
            slowprint('http://www.wtfpl.net/')
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')
            
        elif activity == 6:
            
            new_money = randrange(50,100,10)
            money -= new_money

            if money < 0:
                money = 0

            new_food = randint(1,4)
            food += new_food

            new_mood = randrange(5,10,5)
            mood += new_mood
           

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_money} рублей, +{new_food} шашлыка, +{new_mood} настроения по шкале Шишкаридзе')
            day += 1
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

            new_mood = randrange(10,15,5)
            mood -= new_mood

            if mood < 0:
                mood = 0

            print()
            print(f'ИТОГИ {day} ДНЯ: -{new_money} рублей, -{new_food} шашлыка, -{new_mood} настроения по шкале Шишкаридзе')
            day += 1
            print()
            input('Пизданись головой об клаву, чтобы продолжить...')
            
        if day % 7 == 0:
            print()
            slowprint('Неожиданно Тимур получает сообщение от Иващенко:')
            print()
            slowprint('- Еб вашу мать..агенты хуевы..вы там вообще на месте???')
            slowprint('Отвечай мне на вопрос! Быстро!')
            
            try:                
                index = int(day/7-1)
                quiz = story_quests[index]['quest']
                slowprint(quiz)
                print()
                print('[1] ' + story_quests[index]['answ1'])
                print('[2] ' + story_quests[index]['answ2'])
                print('[3] ' + story_quests[index]['answ3'])
                answer = input()

                if int(answer) == story_quests[index]['correct']:
                    slowprint('Иващенко охуел от такой эрудированности Тимура!')
                    print()
                    slowprint('- Выдать премию этому хлопчику!')
                    print()
                    new_money = randrange(100,200,50)
                    new_mood = randrange(5,10,5)

                    money += new_money
                    mood += new_mood
                    print(f'Тимур получает {new_money} рублей, и настроение сразу лучше стало! На {new_mood} баллов по шкале Шишкаридзе!')
                    print()
                    input('Пизданись головой об клаву, чтобы продолжить...')
                else:
                    slowprint('В общем-то, ничего другого я от вас и не ожидал...')
                    slowprint('-50 очков Гриффиндору!')
                    print()
                    new_mood = randrange(5,15,5)
                    mood -= new_mood
                    slowprint(f'Тимур расстроился из-за твоей тупости! -{new_mood} к настроению!')
                    print()
                    input('Пизданись головой об клаву, чтобы продолжить...')
            except IndexError:
                print('...')
                slowprint('А, хотя в пизду, сам узнаю')
                print()
                input('Пизданись головой об клаву, чтобы продолжить...')
            
        elif day % 3 == 0:
            print()
            slowprint('Неожиданно Тимур вспоминает о своем лучшем друге и скупая слеза скатывается у него по щеке...')
            print()
            new_mood = randrange(10,30,5)
            mood -= new_mood
            print(f'Настроение ухудшилось на -{new_mood} по шкале Шишкаридзе!')
            print()
            
            if new_mood >= 20:
                slowprint('- Бляяя..Да соберись ты, тряпка!')
                print()
            
            input('Пизданись головой об клаву, чтобы продолжить...')
        

        if money == 0 and food == 0 and mood == 0:
            print()
            print(f'ПИЗДА! Како-демон одержал победу на {day} день! Тимур сосет хуй!')
            print()
            slowprint('GAME OVER!!!')
            time.sleep(10)
            break

        clear_output()
        
    if shit_counter >= 10:
        slowprint('Неожиданно, что-то склизкое схватило Тимура за яйца!')
        slowprint("- Неужели, это конец? - лишь промелькнуло в голове у Тимура, когда он резко потянулся рукой и схватил нечто отвратительное, но в то же время прекрасное демоническое запястье!")
        slowprint("Тимур с силой потянул на себя и к своему изумлению, разхреначив в хлам унитаз, достал существо ростом с человека, исторгающее пламя и зловонный запах! Но в прикольной шляпке.") 
        slowprint("- Это КАКО-ДЕМОН 10 уровня!!!")
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
        slowprint('- Тебе пизда, дерьмо-демон!')
        print()
        slowprint('- PASMOTRIM, PIDRRRRRRRRR!!!')
        print()
        a = fight_with_demon()
        
        if a == 1:
            slowprint(f'ПОЗДРАВЛЯЕМ! Это Победа! Тимур расправился с како-демоном за {day} дней!')
            print()
            slowprint('Теперь любой может безбоязненно пойти посрать! А Тимур еще долго в ахуе смотрел на разбитый унитаз и думал, что он будет объяснять Любе...')
            print()
            slowprint('А на следующий день Тимур умер от СПИДа')
            print()
            slowprint('КОНЕЦ')
            
        else:
            slowprint(f'Это фиаско, братан! Како-демон победил тебя на {day} день!')
            print()
            print('GAME OVER!')
    
    
