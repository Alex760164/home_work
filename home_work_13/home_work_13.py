"""
Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и
последнего вхождения.
Понадобятся: срезы, функция replace().
"""

str = input('Введите строку: ')

first_sym_h = str[: str.find('h') + 1: 1]
last_sym_h = str[str.rfind('h'): : 1]
replace_str = str[str.find('h') + 1: str.rfind('h'): 1].replace('h', 'H')
new_str = first_sym_h + replace_str + last_sym_h

print('\nОТВЕТ:\n\t новая строка:', new_str)