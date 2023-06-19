def print_hex(a_input):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Вы ввели {a_input}\n')  # Press Ctrl+F8 to toggle the breakpoint.
    dict_hex = {10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'}
    a = a_input
    list_a = []
    while (a // 16) > 0:
        ostatok = a % 16
        if ostatok > 9:
            list_a.insert(0, dict_hex[ostatok])
        else:
            list_a.insert(0, str(ostatok))
        a = a // 16
    list_a.insert(0,str(a))
    print(f'Число {a_input} в шестнатиричной системе => {("".join(list_a))}')
    print(f'Проверка: {a_input} в шестнатиричной системе => {hex(a_input)}')
