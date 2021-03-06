"""
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
В качестве параметров, функция получает десятичное число и систему счисления.
Возвращает строку - результат перевода десятичного числа.

Подсказка: в этой задаче вам может понадобиться:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не
    придётся разворачивать список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт
    `from string import ascii_uppercase`), она содержит все буквы латинского алфавита.

Алгоритм преобразования десятичного числа в другую систему счисления можно найти в интернете.
Например вот здесь.
"""


def converter_of_numbers(n, b):
    t = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd',
         'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    r = ''
    while n:
        y = n % b
        n = n // b
        r = t[y]+r
    return r


print('Number Convert')
number = int(input('Введите число для преобразования:'))
system = int(input('Введите систему исчисления (от 2 - до 32):'))

if 2 <= system <= 32:
    print('\nОТВЕТ:',
          '\n\tВходное число - ', number,
          '\n\tСистема исчисления - ', system,
          '\n\tВыходное число - ', converter_of_numbers(number, system))
else:
    print('ОТВЕТ: \n\t Такой системы исчисления не существует.')
