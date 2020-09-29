"""
Дан текст (много строк в одном вводе) состоящий из нескольких строки. Выведите слово, которое в этом
тексте встречается чаще всего. Если таких слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""
from pprint import pprint

special_symbol = ['!', '@', '#', '№', '$', '%', '^', '&', '*',
                  '(', ')', '-', '_', '=', '+', '{', '}', '[',
                  ']', '|', '\\', '>', '<', '/', '?', '.', ',',
                  '\'', '\"', '`', '~', ':', ';', '»', '«', '—']

print('Для поиска количества совпадений слов.')
text = input('Введите текст: ')
lst = ''.join([char for char in text if char not in special_symbol]).lower().split()

d = {}
for word in lst:
    d[word] = d.get(word, 0) + 1
pprint(d)

max_value = max(d.values())
max_key = ''
for key, value in d.items():
    if value == max_value:
        max_key = key
print('ОТВЕТ:\n\t', 'Cлово: \"', max_key, '\" повторяется ', max_value, 'раз(-а).')