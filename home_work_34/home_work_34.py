"""
В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки. (исходный файл прикреплён к уроку)
Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу.
Так же, записать в новый файл всех учащихся в формате "Фамилия И.    Ср. балл":
"""


def one_sub(text):
    text.split()
    result = ' '.join(text.split())
    return result


src = open('src.txt', 'r', encoding='utf-8')
new_src = open('new_src.txt', 'w', encoding='utf-8')

tmp_list = []
new_list = []
while True:
    data = src.readline()
    if data:
        tmp_list = one_sub(data).split(' ')
        full_name = tmp_list[0]
        name = tmp_list[0][0] + '.'
        first_name = tmp_list[1]
        sum_ball = sum(list(map(int, tmp_list[2:])))
        col_ball = len(list(map(int, tmp_list[2:])))
        avr_ball = round(sum_ball/col_ball, 2)
        new_src.write(first_name + ' ' + name + '\t' + str(avr_ball) + '\n')
        new_list.append([first_name, full_name, avr_ball])
    else:
        break
src.close()

print('ОТВЕТ:\nСписок учеников у которых средний бал меньше 5:')
for i in range(len(new_list)):
    if new_list[i][2] < 5:
        print('\t' + new_list[i][0] + ' ' + new_list[i][1] + ' ' + str(new_list[i][2]))

print('\nСредний балл по классу: ', end='')
summ = 0
for i in range(len(new_list)):
    summ = summ + new_list[i][2]
group_avr_ball = round(summ / len(new_list), 2)
print(group_avr_ball)
