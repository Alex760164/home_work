"""
Написать функцию, принимающую ТРИ параметра и выполняющая циклически сдвиг целого числа (первый параметр)
на N разрядов (второй параметр) вправо или влево, в зависимости от значения третьего параметра функции.
Третий параметр булевский, задаёт направление сдвига (по умолчанию влево (False)).
"""


def cyclic_shift(number, step, direction=False):
    number = str(number)
    if direction:
        number = number[-step:] + number[:-step]
    else:
        number = number[step:] + number[: step]
    return number


numb = int(input('Введите число: '))
shift = int(input('Введите количество разрядов: '))
param = input('Укажите направление сдвига (Лево - (l)/ Вправо - (r)): ')

if param == 'l':
    print('ОТВЕТ:', '\n\tВходное число: ', numb, '\n\tВыходное число: ', cyclic_shift(numb, shift, False))
elif param == 'r':
    print('ОТВЕТ:', '\n\tВходное число: ', numb, '\n\tВыходное число: ', cyclic_shift(numb, shift, True))
else:
    print('ОТВЕТ:', '\n\tВходное число: ', numb, '\n\tВыходное число: ', cyclic_shift(numb, shift))
