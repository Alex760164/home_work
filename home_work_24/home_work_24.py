"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время
года (в виде строки), которому этот месяц принадлежит (зима, весна, лето или осень).
"""


def season(s):
    if 1 <= s <= 12:
        if s in (1, 2, 12):
            res = 'Зима ' + '\U00002744'
        elif s in (3, 4, 5):
            res = 'Весна ' + '\U0001F338'
        elif s in (6, 7, 8):
            res = 'Лето ' + '\U00002600'
        else:
            res = 'Осень ' + '\U0001F327'
    else:
        res = 'Невозможно определить время года'
    return res


def months(m):
    if 1 <= m <= 12:
        if m == 1:
            res = 'Январь'
        elif m == 2:
            res = 'Февраль'
        elif m == 3:
            res = 'Март'
        elif m == 4:
            res = 'Апрель'
        elif m == 5:
            res = 'Май'
        elif m == 6:
            res = 'Июнь'
        elif m == 7:
            res = 'Июль'
        elif m == 8:
            res = 'Август'
        elif m == 9:
            res = 'Сентябрь'
        elif m == 10:
            res = 'Октябрь'
        elif m == 11:
            res = 'Ноябрь'
        else:
            res = 'Декабрь'
    else:
        res = 'Неизвестный месяц.'
    return res


month = int(input('Введите номер месяца: '))
print('ОТВЕТ:\n\t' + str(month) + '-й месяц это \"' + months(month) + '\", а время года - ' + season(month))
