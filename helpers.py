from data import *
from time import sleep
from random import randint


def fight (current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print(f'{enemy ["phrase"]}')
    input('Enter чтобы продолжить')
    print ()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint (1, 100)
            if crit <= player ['luck']:
                enemy_hp -= player ['damage'] * 3
            else:
                enemy_hp -= player['damage']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['damage'] * player ['armor']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        player ['money'] += enemy ['money']
        print (player)
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    return current_enemy

def train (training_type):
    training_type = input('''1 - тренировать атаку
2 - тренировать оборону
3 - тренировать здоровье
''')
    if training_type == '1':
        player ['damage'] += 1
        print (f'Тренировка окончена. Ваши характеристики: {player}')

    elif training_type == '2':
        player ['armor'] -=  0.05
        print (f'Тренировка окончена. Ваши характеристики: {player}')

    elif training_type == '3':
        player ['hp'] += 5
        print (f'Тренировка окончена. Ваши характеристики: {player}')


def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["damage"]}. Шанс критического урона ({player["damage"] * 3}ед.) равен {player["luck"]}%')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
    print()



def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["damage"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print()

def store():
    for name, data in shop.items():
        print(f'{name}:')
        for key, value in data.items():
            print(f'    {key} - {value}')
        print()

    purchase = input('Выберите предмет для покупки, либо напишите закрыть: ')

    if purchase == 'Меч из хлеба':
        if player['money'] >= 50:
            player['damage'] += 5
            player['money'] -= 50
            print(f'Покупка прошла успешна! {player}')
        else:
            print('Не хватает монет')

    elif purchase == 'Броня из хлеба':
        if player['money'] >= 100:
            player['hp'] += 50
            player['money'] -= 100
            print(f'Покупка прошла успешна! {player}')
        else:
            print('Не хватает монет')

    elif purchase == 'Меч великого пельменя':
        if player['money'] >= 150:
            player['damage'] += 20
            player['money'] -= 150
            print(f'Покупка прошла успешна! {player}')
        else:
            print('Не хватает монет')

    elif purchase == 'Броня великого пельменя':
        if player['money'] >= 200:
            player['hp'] += 150
            player['money'] -= 200
            print(f'Покупка прошла успешна! {player}')
        else:
            print('Не хватает монет')

    else:
        print('Магазин закрыт')
