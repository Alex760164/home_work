"""
Веселая ГЕОМЕТРИЯ :)
"""

import sys


# Фигура №1
def triangle_1(char, h):
    for i in range(h+1):
        for j in range(i):
            print(char + ' ', end='')
            j += 1
        print()
        i += 1


# Фигура №2
def triangle_2(char, h):
    print()
    cols = rows = h
    for i in range(rows):
        for j in range((2 * cols) - 1):
            if (j >= (cols - 1 - i)) and (j <= (cols - 1 + i)) or i == rows - 1:
                print(char + ' ', end='')
            else:
                print('  ', end='')
            j += 1
        print()
        i += 1


# Фигура №3
def triangle_3(char, h):
    print()
    cols = rows = h
    for i in range(rows):
        for j in range((2 * cols) - 1):
            if ((rows - 1) - j) == i or (j - (rows - 1) == i) or i == rows - 1:
                print(char + ' ', end='')
            else:
                print('  ', end='')
            j += 1
        print()
        i += 1


# Фигура №4
def square_1(char, h):
    print()
    cols = h
    rows = h
    for i in range(rows):
        for j in range(cols):
            print(char + '  ', end='')
            j += 1
        print()
        i += 1


# Фигура №5
def square_2(char, h):
    print()
    cols = h
    rows = h
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print(char + '  ', end='')
            else:
                print('   ', end='')
            j += 1
        print()
        i += 1


# Фигура №6
def rhombus_1(char, h):
    print()
    cols = h
    rows = h
    for i in range(rows):
        for j in range(cols):
            if i <= rows // 2:
                if (j >= ((cols // 2) - i)) and (j <= ((cols // 2) + i)):
                    print(char + ' ', end='')
                else:
                    print('  ', end='')
            elif j == (cols // 2) - (rows - 1 - i) or j == (cols // 2) + (cols - 1 - i):
                print(char + ' ', end='')
            else:
                print('  ', end='')
            j += 1
        print()
        i += 1


# Фигура №7
def rhombus_2(char, h):
    print()
    cols = h
    rows = h
    for i in range(rows):
        for j in range(cols):
            if i <= rows // 2:
                if (j >= ((cols // 2) - i)) and (j <= ((cols // 2) + i)):
                    print(char + ' ', end='')
                else:
                    print('  ', end='')
            elif j == cols // 2 or j == (cols // 2) - (rows - 1 - i) or j == (cols // 2) + (cols - 1 - i):
                print(char + ' ', end='')
            else:
                print('  ', end='')
            j += 1
        print()
        i += 1


print('ВЕСЕЛАЯ ГЕОМЕТРИЯ'
      '\nЭта программа предназначенная для рисования следующих геометрических фигур:'
      '\n\tФигура №1 - Прямоугольный треугольник (закрашенный).'
      '\n\tФигура №2 - Равнобедренный треугольник (закрашенный).'
      '\n\tФигура №3 - Равнобедренный треугольник (не закрашенный).'
      '\n\tФигура №4 - Квадрат (закрашенный).'
      '\n\tФигура №5 - Квадрат (не закрашенный).'
      '\n\tФигура №6 - Ромб (на половину закрашенный).'
      '\n\tФигура №7 - Ромб (на половину закрашенный с полосой).\n')

run_stop = ''
while run_stop not in ('y', 'n'):
    run_stop = input('Хотите продолжить (y / n): ')

if run_stop == 'y':
    print('ОТЛИЧНО!!! Вам понравится.\n\nНу что ПОЕХАЛИ...\n\nШАГ.1. Выберете нужную фигуру. ')
    num_figure = int(input('Для этого нужно просто указать ее номер №'))
    if num_figure:
        print('\nОтлично. Переходим к следующему шагу.\n\nШАГ.2. Выберете нужную высоту фигуры.'
              '\nСОВЕТ: Для корректного отображения используйте значение высоты больше 5\n')
    height = int(input('Укажите высоту фигуры: '))
    if height % 2 != 0:
        print('\nОтлично. Переходим к следующему шагу.\n\nШАГ.3. Выберете нужную высоту фигуры. ')
    else:
        print('ОШИБКА!!!\n\tДля отображения геометрических фигур введите нечётное число.')
        height = int(input('Укажите высоту фигуры: '))
        if height % 2 == 0:
            height = height + 1
        print('\nОтлично. Переходим к следующему шагу.\n\nШАГ.3. Выберете любой символ на клавиатуре.\n')
    symbol = input('Укажите символ: ')

    print('\nРЕЗУЛЬТАТ')

    if num_figure == 1:

        # Фигура №1 - Прямоугольный треугольник (закрашенный).
        print('\nФигура №1 - Прямоугольный треугольник (закрашенный).')
        triangle_1(symbol, height)

    elif num_figure == 2:

        # Фигура №2 - Равнобедренный треугольник (не закрашенный).
        print('\nФигура №2 - Равнобедренный треугольник (закрашенный).')
        triangle_2(symbol, height)

    elif num_figure == 3:

        # Фигура №3 - Равнобедренный треугольник (не закрашенный).
        print('\nФигура №3 - Равнобедренный треугольник (не закрашенный).')
        triangle_3(symbol, height)

    elif num_figure == 4:

        # Фигура №4 - Квадрат (закрашенный).
        print('\nФигура №4 - Квадрат (закрашенный).')
        square_1(symbol, height)

    elif num_figure == 5:

        # Фигура №5 - Квадрат (не закрашенный).
        print('\nФигура №5 - Квадрат (не закрашенный).')
        square_2(symbol, height)

    elif num_figure == 6:

        # Фигура №6 - Ромб (на половину закрашенный)
        print('\nФигура №6 - Ромб (на половину закрашенный)')
        rhombus_1(symbol, height)

    elif num_figure == 7:

        # Фигура №7 - Ромб (на половину закрашенный с полосой)
        print('\nФигура №7 - Ромб (на половину закрашенный с полосой)')
        rhombus_2(symbol, height)

    else:

        print('Под таким номером геометрической фигуры нет!')
        sys.exit()
else:
    sys.exit()
