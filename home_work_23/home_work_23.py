"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""


def square(length):
    if length > 0:
        perimeter = 4 * length
        area = length ** 2
        diagonal = length * 2 ** (1 / 2)
        result = (perimeter, area, diagonal)
        return result
    else:
        return False


argument = int(input('Введите размер стороны квадрата: '))

if square(argument):
    print('ОТВЕТ:\n\t', square(argument), type(square(argument)))
else:
    print('ОТВЕТ:\n\tВведите число больше 0')
