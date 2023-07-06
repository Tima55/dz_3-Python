"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os


def parse_file_path(file_path):
    # Получаем путь к файлу
    directory = os.path.dirname(file_path)
    # Получаем имя файла с расширением
    filename = os.path.basename(file_path)
    # Разделяем имя файла и расширение
    name, extension = os.path.splitext(filename)

    return directory, name, extension


# Пример использования функции
file_path = '/path/to/file.txt'
path, name, extension = parse_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)
