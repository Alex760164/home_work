"""
В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки. (исходный файл прикреплён к уроку)
Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу.
Так же, записать в новый файл всех учащихся в формате "Фамилия И.    Ср. балл":
"""

src = open('src.txt', 'r', encoding='utf-8')
new_src = open('new_src.txt', 'w', encoding='utf-8')
format_print = '{fio:<25} {avr_ball:>10.2}'

total = 0
count = 0
print('ОТВЕТ:\nСписок учеников у которых средний бал меньше 5:')

while True:
    data = src.readline()
    if data:
        tmp_list = data.strip('\n').split()
        full_name = tmp_list[0]
        name = tmp_list[0][0] + '.'
        first_name = tmp_list[1]
        avr_ball = sum(list(map(int, tmp_list[2:])))/len(tmp_list[2:])
        res_for_file = format_print.format(fio=first_name + ' ' + name, avr_ball=avr_ball)
        res_on_screen = format_print.format(fio=first_name + ' ' + full_name, avr_ball=avr_ball)
        new_src.write(res_for_file + '\n')
        if avr_ball < 5:
            print('\t' + res_on_screen)
        total += avr_ball
        count += 1
    else:
        break

print('\nСредний балл по классу: ', round(total / count, 2))
new_src.close()
src.close()
