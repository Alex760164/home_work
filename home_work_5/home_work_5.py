"""
В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же
время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть не
больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их
хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
Использовать только арифметические операторы. Оператор IF не понадобится. Подсказка: используйте операторы //, % и +
"""

class_1 = int(input('\nВведите количество учеников в классе №1: '))
class_2 = int(input('Введите количество учеников в классе №2: '))
class_3 = int(input('Введите количество учеников в классе №3: '))
kol_user = 2 # количество учеников за партой.

kol_desks_1 = (class_1 // kol_user) + (class_1 % kol_user) # количество парт в классе №1.
kol_desks_2 = (class_2 // kol_user) + (class_2 % kol_user) # количество парт в классе №2.
kol_desks_3 = (class_3 // kol_user) + (class_3 % kol_user) # количество парт в классе №3.
vsego = kol_desks_1 + kol_desks_2 + kol_desks_3

print('\nОТВЕТ:',
      '\n\tДля класса №1 нужно закупить - ', kol_desks_1, 'парт.',
      '\n\tДля класса №2 нужно закупить - ', kol_desks_2, 'парт.',
      '\n\tДля класса №3 нужно закупить - ', kol_desks_3, 'парт.',
      '\n\tВсего для 3-х классов нужно закупить - ', vsego, 'парт.')