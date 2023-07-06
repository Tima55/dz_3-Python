'''Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
'''

'''Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.'''

from random import randint
import random


def create_position():
    simbol = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ])
    digit = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', ])
    position = simbol + digit
    # print(position)
    return position


def gen_positions():
    eigth_ferz_list = [create_position()]

    while len(eigth_ferz_list) < 9:
        new_position = create_position()
        if new_position not in eigth_ferz_list:
            eigth_ferz_list.append(new_position)
    return eigth_ferz_list


def gen_broken_field(position: str) -> list:
    simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
    digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
    horisont_, vertic_ = list(position)

    broken_field_h = [horisont_ + i for i in digit_ if i != vertic_]
    broken_field_v = [i + vertic_  for i in simbol_ if i != horisont_]

    result =   broken_field_h +  broken_field_v

    return result


def add(x, y):
    return list(map(lambda a, b: a + b, x, y))

def test_hor_vert(variant_position: list) -> bool:
    result = True

    return result


variant_position = gen_positions()

a, b = list(variant_position[1])

print(variant_position)
print(variant_position[1])
print(a, b)

print(gen_broken_field(variant_position[1]))





# step = simbol_.index(a) + 1

def levo_niz(position_ferz):
    simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
    digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
    digit_poz, simbol_poz = list(position_ferz)
    # --- срез внизлево---
    spisok_ostavsh_cifr_ = digit_[:int(simbol_poz) - 1]
    spisok_ostavsh_simb_ = simbol_[:simbol_.index(digit_poz)]
    # print(spisok_ostavsh_cifr_)
    # print(spisok_ostavsh_simb_)
    # print('---')

    if len(spisok_ostavsh_cifr_) < len(spisok_ostavsh_simb_):
    #     -----режем цифры иначе - буквы
        new_simb = (spisok_ostavsh_simb_[-len(spisok_ostavsh_cifr_):])
        new_cif = (spisok_ostavsh_cifr_)

    else:
        new_cif = (spisok_ostavsh_cifr_[-len(spisok_ostavsh_simb_):])
        new_simb = (spisok_ostavsh_simb_)

    if len(spisok_ostavsh_simb_) != 0 and len(spisok_ostavsh_cifr_) !=0:
    # --- склеить два списка----
        print(new_simb)
        print(new_cif)
        result_ln = add(new_simb, new_cif)

    else: result_ln = []

    return result_ln

def pravo_niz(position_ferz):
    simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
    digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
    digit_poz, simbol_poz = list(position_ferz)
    # --- срез внизлево---
    spisok_ostavsh_cifr_ = digit_[:int(simbol_poz) - 1]
    spisok_ostavsh_simb_ = simbol_[:simbol_.index(digit_poz)]
    # print(spisok_ostavsh_cifr_)
    # print(spisok_ostavsh_simb_)
    # print('---')

    if len(spisok_ostavsh_cifr_) < len(spisok_ostavsh_simb_):
    #     -----режем цифры иначе - буквы
        new_simb = (spisok_ostavsh_simb_[-len(spisok_ostavsh_cifr_):])
        new_cif = (spisok_ostavsh_cifr_)

    else:
        new_cif = (spisok_ostavsh_cifr_[-len(spisok_ostavsh_simb_):])
        new_simb = (spisok_ostavsh_simb_)

    if len(spisok_ostavsh_simb_) != 0 and len(spisok_ostavsh_cifr_) !=0:
    # --- склеить два списка----
        print(new_simb)
        print(new_cif)
        result_ln = add(new_simb, new_cif)

    else: result_ln = []

    return result_ln


print(levo_niz(variant_position[1]))
print('ssssssssssssssssss')

simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
digit_poz, simbol_poz = list(variant_position[1])
# --- срез внизлево---
spisok_ostavsh_cifr_pr_niz = digit_[:int(simbol_poz) - 1]
spisok_ostavsh_simb_ = simbol_[:simbol_.index(digit_poz)]
# print(spisok_ostavsh_cifr_)
# print(spisok_ostavsh_simb_)
# print('---')

if len(spisok_ostavsh_cifr_) < len(spisok_ostavsh_simb_):
    #     -----режем цифры иначе - буквы
    new_simb = (spisok_ostavsh_simb_[-len(spisok_ostavsh_cifr_):])
    new_cif = (spisok_ostavsh_cifr_)

else:
    new_cif = (spisok_ostavsh_cifr_[-len(spisok_ostavsh_simb_):])
    new_simb = (spisok_ostavsh_simb_)

if len(spisok_ostavsh_simb_) != 0 and len(spisok_ostavsh_cifr_) != 0:
    # --- склеить два списка----
    print(new_simb)
    print(new_cif)
    result_ln = add(new_simb, new_cif)

else:
    result_ln = []
