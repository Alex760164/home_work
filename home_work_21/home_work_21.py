"""
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
быть произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент:
+ сложить их; - вычесть; * умножить; / разделить (первое на второе). В остальных случаях вернуть строку
 "Неизвестная операция".
"""


def arithmetic(par_1, par_2, par_3):
    if par_3 == '+':
        res = par_1 + par_2
        return res
    elif par_3 == '-':
        res = par_1 - par_2
        return res
    elif par_3 == '*':
        res = par_1 * par_2
        return res
    elif par_3 == '/':
        res = par_1 / par_2
        return res
    else:
        res = 'unknown'
        return res


p1 = int(input('Введите 1-е число: '))
p2 = int(input('Введите 2-е число: '))
p3 = input('Введите арифметическую операцию: ')

result = arithmetic(p1, p2, p3)

if result != 'unknown':
    print('ОТВЕТ:\n\t', p1, p3, p2, '=', result)
else:
    print('ОТВЕТ:\n\tНеизвестная операция')
