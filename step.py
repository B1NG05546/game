from helpers import *

name = input('Введи своё имя, путник: ')
player['name'] = name

print("Привет, {}, добро пожаловать в игру!".format(name))
input("Нажмите Enter, чтобы продолжить...")

current_enemy= 0

while True:
    action = input('''Выбери действие:
    1 - В бой!
    2 - Тренировка
    3 - Магазин
    4 - Статистика игрока
    5 - Статистика врага : ''')

    if action == '1':
        current_enemy = fight(current_enemy)
        
        if current_enemy == 3:
            break

    elif action == '2':

        train('1')

    elif action == '3':
        store()

    elif action == '4':
        display_player()

    elif action == '5':
        display_enemy(current_enemy)
