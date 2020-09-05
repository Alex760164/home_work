"""
Написать программу, которая выводит в консоль таблицу Escape-последовательностей.
"""

title = 'Escape sequences'
a = '\\a\t\t Bell (alert)'
b = '\\b\t\t Backspace'
n = '\\n\t\t New line'
t = '\\t\t\t Horizontal tab'
bs = '\\\\\t\t Backslash \\'
dqm = '\\\"\t\t Double quotation mark \"'
sqm = '\\\'\t\t Single quotation mark \''

print('\n' + title + '\n' + a + '\n' + b + '\n' + n + '\n' + t + '\n' + bs + '\n' + dqm + '\n' + sqm)