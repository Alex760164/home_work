"""
Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True,
если год високосный, и False иначе.
"""


def is_year_leap(y):
    if y % 4 != 0:
        return False
    else:
        if y % 100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            else:
                return True


year = int(input('Введите год для проверки: '))

if is_year_leap(year):
    print('ОТВЕТ:\n\t', year, 'год - Высокосный год')
else:
    print('ОТВЕТ:\n\t', year, 'год - Не высокосный год')
