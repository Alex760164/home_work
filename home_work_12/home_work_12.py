
s = input('Введите строку: ')
ch = input('Введите символ для поиска: ')

print('ОТВЕТ:')
idx = 0
for i in range(len(s)):
    idx = s.find(ch, i)
    if s[i] == ch:
        print('\tИндекс элемента: ', idx, '\tНомер эелемента в тексте: ', idx + 1)
    if idx == -1:
        break