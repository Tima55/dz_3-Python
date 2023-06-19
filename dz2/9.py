'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''


a = (input('Введите 1ю дробь в виде: "1/2" => '))
b = (input('Введите 2ю дробь в виде: "1/2" => '))

def trnslate(data):
    data_chislit = int(data.split('/')[0])
    data_znamenat = int(data.split('/')[1])
    return data_chislit, data_znamenat

def data_sum(a, b):
    a_ch = trnslate(a)[0]
    a_zn = trnslate(a)[1]
    b_ch = trnslate(b)[0]
    b_zn = trnslate(b)[1]

    # print(f'{a_ch * b_zn + b_ch * a_zn}/{b_zn * a_zn}')
    ch = a_ch * b_zn + b_ch * a_zn
    zn = b_zn * a_zn
    res = output(ch, zn)
    return res

def data_mult(a, b):
    a_ch = trnslate(a)[0]
    a_zn = trnslate(a)[1]
    b_ch = trnslate(b)[0]
    b_zn = trnslate(b)[1]

    # print(f'{a_ch * b_ch}/{a_zn * b_zn}')
    res = output(a_ch * b_ch, a_zn * b_zn)
    return res

def output(ch1,zn1):
    dd = f'{ch1}/{zn1}'
    return dd


print(f'{a} * {b} = {data_mult(a, b)}')
print(f'{a} + {b} = {data_sum(a, b)}')
