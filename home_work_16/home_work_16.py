"""
Дан список из чисел и индекс элемента в списке `k`. Удалите из списка элемент с индексом `k`, сдвинув
влево все элементы, стоящие правее элемента с индексом `k`.
Программа получает на вход список (список можно создать и заполнить случайными числами), затем число `k`.
Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода `pop()`
(да, такой метод есть в арсенале списков. Я ошибочно сказал, что его нет. pop() без параметра, удаляет
последний элемент списка и возвращает его значение) без параметров.
Программа должна осуществлять сдвиг непосредственно в списке.
Также нельзя использовать дополнительный список.
Также не следует использовать метод `pop(k)` с параметром.
Использовать оператор del НЕЛЬЗЯ!
"""
import random

lst_1 = [random.randint(10, 21) for _ in range(9)]
print('Список из чисел для for:', lst_1, 'длина списка:', len(lst_1), 'элементов')
k = int(input('Введите индекс элемента в диапазоне (от 0 и до ' + str(len(lst_1)-1) + '): '))

if k > len(lst_1)-1:
    print('ОШИБКА! Введен индекс элемента больше чем max индекс в списке')
else:
    for i in range(k + 1, len(lst_1)):
        lst_1[i - 1] = lst_1[i]
        i += 1
    lst_1.pop()
    print('ОТВЕТ:\n\tСписок из чисел после:  ', lst_1, 'длина списка:',
          len(lst_1), 'элемнтов', type(lst_1))
