"""
Дан словарь ключами которого являются английские слова, а значениями - списки латинских слов.
Необходимо развернуть словарь. Другими словами, необходимо, на основании заданного словаря, создать
новый словарь, у которого в качестве ключей будут взяты латинские слова, из первого словаря,
а значениями будут, соответствующие им, английские слова.
"""
from pprint import pprint

old_dict = {'apple': ['malum', 'pomum', 'popula'],
            'fruit': ['baca', 'bacca', 'popum'],
            'punishment': ['malum', 'multa']}

new_dict = {key: [i for i in old_dict.keys() if key in old_dict[i]] for j, key in old_dict.items() for key in key}

print('ОТВЕТ:\nВходной словарь:')
pprint(old_dict)
print('\nВыходной словарь:')
pprint(new_dict)
