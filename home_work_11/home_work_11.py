"""
Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
Используйте для решения задачи функцию `count()`
"""

str = input('Введите строку: ')

count_words = str.strip().count(' ') + 1

print('ОТВЕТ: \n\t',
      '- количество слов в строке:', count_words)