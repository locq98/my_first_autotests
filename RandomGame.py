while (range):
    from random import randint
    print('\nМеня зовут Ярослав. Я создатель этой игры. Я загадал число от 1 до 5. Сможете отгадать?')
    player_1 = int(input('Введите ваше число: '))
    random_list = randint(1,5)
    if player_1 == random_list:
        print('Ура! Твое число совпало! Я загадал: ' + str(random_list))
    elif int(player_1) >= 6:
        print('Извините, вы ввели число больше 5. Попробуйте сначала')
    else:
        print('Увы... Я загадал: ' + str(random_list))
