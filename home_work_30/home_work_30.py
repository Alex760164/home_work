"""
Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, и B,
соответственно, на A. Замену можно производить ТОЛЬКО используя функцию replace().
В результате применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA
Использовать циклы и оператор IF запрещено.
"""


def replace_string(string, old_char, new_char):
    tmp_1 = string.replace(old_char,  'tmp_char')
    tmp_2 = tmp_1.replace(new_char, old_char)
    res = tmp_2.replace('tmp_char', new_char)
    return res


chars = input('Введите строку: ').upper()
old_symbol = input('Введите заменяемый символ: ').upper()
new_symbol = input('Введите новый символ: ').upper()

print('ОТВЕТ:\n\tВходная строка: ', chars)
print('\tСтарый символ:  ', old_symbol, '\n\tНовый символ:   ', new_symbol, )
print('\tВыходная строка:', replace_string(chars, old_symbol, new_symbol))
