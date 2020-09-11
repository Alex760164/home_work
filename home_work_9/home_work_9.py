"""
Программа запрашивает ввод, с клавиатуры, целые числа, пока не будет введён 0. Как только будет введён 0 (ноль),
программа должна посчитать и вывести на экран:
    - количество введённых чисел (завершающий 0 не считается)
    - их сумму
    - среднее арифметическое всех введённых чисел(не считая завершающего числа 0)
    - определить максимальное и минимальное значение
    - определить количество чётных и не чётных элементов в последовательности
"""

print('Введите целое число:')

number = int(input())
count = 1
summa = number
max = number
min = number

while number != 0:
    number = int(input())
    if number > 0:
        count += 1
        summa += number
        if number > max:
            max = number
        if (number < max) and (number < min):
            min = number

    average = summa / count

print ('ОТВЕТ:',
       '\n\tКол. введённых чисел:\t', count,
       '\n\tСумма введённых чисел:\t', summa,
       '\n\tСреднее арифметическое:\t', average,
       '\n\tМаксимальное число:\t', max,
       '\n\tМинимальное число:\t', min)