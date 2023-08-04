'''
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
'''

import logging
from datetime import  datetime, date


logging.basicConfig(filename='Task4.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

months = {'янв': 1, 'фев': 2,'мар': 3,'апр': 4,'май': 5,'июн': 6,'июл': 7,'авг': 8,'сен': 9,'окт': 10,'ноя': 11,'дек': 12}
weekdays = {'пон': 1, 'вто': 2,'сре': 3,'чет': 4,'пят': 5,'суб': 6,'вос': 7}

def text_to_date(text: str):
    '''Переводим текст в объект дату'''
    try:
        year = datetime.now().year                     # 2023
        count, weekday_, month_ = text.split()            # 3-я среда мая - текстовый формат
        month = months[month_[:3]]                       # 5 - число
        weekday = weekdays[weekday_[:3]] - 1             # 2 - число
        count = int(count[0])
    except Exception as exc:
        logger.info(f'{count}-й  {weekday_}  {month_} {year} =  ошибка: {exc}')

    count_week = 0
    for day in range (1, 31 + 1):
        rezult = date(year=year, month=month, day=day)
        if rezult.weekday() == weekday:
            count_week += 1
            if count_week == count:
                logger.info(f'{count}-й {weekday_} {month_} {year} = {rezult} ')
                return rezult

'''
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
'''

from Task4 import text_to_date
import  argparse
from  datetime import datetime

if __name__ == '__main__':
    months = { 1: 'янв',  2: 'фев' ,  3: 'мар',  4:  'апр', 5: 'май', 6: 'июн' ,  7: 'июл',  8: 'авг',  9: 'сен',  10: 'окт',
               11: 'ноя',  12: 'дек'}
    weekdays = {1: 'вто', 2: 'сре', 3: 'чет', 4: 'пят', 5: 'суб', 6: 'вос', 7: 'пон'}

    parser = argparse.ArgumentParser(description="Получаем строку с датой")
    parser.add_argument('-count', type=str, default='1')
    parser.add_argument('-weekday', type=str, default='понeдельник')
    parser.add_argument('-month', type=str, default=months[datetime.now().month])

    args = parser.parse_args()

    weekday = weekdays[int(args.weekday)]  if  args.weekday.isdigit() and int(args.weekday) in weekdays else args.weekday   # неделю можно вводить числом
    month = months[int(args.month)] if args.month.isdigit() and int(args.month) in months else args.month  # месяц можно вводить числом

    print(f'{args.count} {weekday} {month}: ', text_to_date(f'{args.count} {weekday} {month}'))

    # запуск с командной строки: python Seminar_15/Task5.py -count='3-я' -weekday='среда'
    #  запуск с командной строки: python Seminar_15/Task5.py -count='3-я' -weekday=3
#  запуск с командной строки: python Seminar_15/Task5.py -count='3-я' -weekday=3 - month=3




if __name__ == '__main__':
    print('2-й вторник мая:', text_to_date('2-й понедельник май'))
    print('3-й четверг ноября:', text_to_date('3-й вторник ноября'))
    print('4-я среда мая:', text_to_date('4-я среда май'))
