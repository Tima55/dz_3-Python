'''напишите программу банкомата
 начальная сумма равна 0
 допустимые действия пополнить снять выйти 
 сумма пополнения и снятия кратны 50 у е
 проценты за снятие 1,5 % от суммы снятия но не менее 30 и не более 600 у е 
 после каждой 3 операции пополнение или снятие начисляеться 3 %
 незьзя снять больше чем на счете 
 при привышении в 5млн вычитаеться налог в 10 % перед каждой операцией 
 любое действие выводит сумму денег
'''
from itertools import repeat
T = 0 # Вывод 
s = 0 # Счетчик операций
Limit = 5000000 # Лимит на 10% 
print('Важная информация! Банкомат принимает и выдаёт купюры только по 50$')
for _ in repeat(0):
    print("Наличные на счёте: ", T ,'$')
    print('1-Внести наличные\n2-Снять наличные\n3-Выйти')
    N = int(input("Введите номер операции: "))
    if N == 1: # Внесение наличных
        s+=1
        CashSum=int(input("Внесение наличных: "))
        if CashSum%50==0: # Проверка кратности 50
            T = CashSum+T # Сумма без вычета % 
            if T>Limit:
                T2 = CashSum*0.1 # Вычесление 10%
                T = T - T2
                print('Вычет 10% за операцию: ',"%.2f" %T2,'$')
            elif s%3==0 and T<Limit:
                T2 = CashSum*0.03 # Вычесление 3%
                T = T - T2
                print('Вычет 3% за операцию: ',"%.2f" %T2,'$')
    if N == 2: # Снятие наличных
        s+=1
        print('Важная инофрмация! Ограничение по сумме снятие от 30$ до 600$')
        CashWit=int(input("Снятие наличных : "))
        if CashWit<=T:
            if CashWit%50==0: # Проверка кратности 50
                T = T - CashWit # Снятие  без вычета %
                if T>Limit:
                    T2 = CashWit*0.1 # Вычесление 10%
                    T = T - T2
                    print('Вычет 10% за операцию: ',"%.2f" % T2,'$')
                elif s%3==0 and T<Limit:
                    T2 = CashWit*0.03 # Вычесление 3%
                    T = T - T2
                    print('Вычет 3% за операцию: ',"%.2f" % T2,'$')
                elif CashWit>=30 and CashWit<=600:
                    T2=CashWit*0.015 # Вычесление 1.5%
                    T=T-T2
                    print('Вычет 1.5% за операцию: ',"%.2f" % T2,'$')
            else:
                print('Банкомат выдыёт купюры только по 50$')        
        else:
            print('Не достаточно средств!')            
    if N == 3:
        print('Заберите карту.')
        break    