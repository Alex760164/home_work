"""
Веселая ГЕОМЕТРИЯ :)
"""


# Треугольник №1
def triangle(char, h):
    for i in range(h):
        print(' ' * (h - i - 1) + char * (2 * i + 1))


# Треугольник №2
def triangle_2(char, h):
    for i in range(h+1):
        for j in range(i+1):
            print(char + ' ', end='')
            j += 1
        print()
        i += 1


# Квадрат
def square(char, h):
    print()
    cols = h
    rows = h
    for i in range(rows):
        for j in range(cols):
            print(char + ' ', end='')
            j += 1
        print()
        i += 1


# Ромб №1
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


# Ромб №2
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


height = int(input('Укажите высоту фигуры: '))
symbol = input('Укажите символ: ')

if height % 2 != 0:
    # Треугольник №1
    print('\nТреугольник №1')
    triangle(symbol, height)

    # Треугольник №2
    print('\nТреугольник №2')
    triangle_2(symbol, height)

    # Квадрат
    print('\nКвадрат')
    square(symbol, height)

    # Ромб №1
    print('\nРомб №1')
    rhombus_1(symbol, height)

    # Ромб №2
    print('\nРомб №2')
    rhombus_2(symbol, height)
else:
    print('ОШИБКА!!!\n\tДля отображения геометрических фигур введите нечётное число.')
