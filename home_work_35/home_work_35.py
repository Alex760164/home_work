"""
Реализовать класс цифрового счетчика. Обеспечьте возможность установки максимального и минимального значений,
увеличения счетчика на 1, возвращения текущего значения.
"""


class MyCounter:
    def __init__(self, begin, end):
        self.current = self.begin = begin
        self.end = end

    def increment(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            return 'Out of range'


min_num = int(input('Установите min. значение: '))
max_num = int(input('Установите max. значение: '))
my_count = MyCounter(begin=min_num, end=max_num)

print('ОТВЕТ:\n\tmin->(' + str(min_num) + ') ', end='')
for i in range(min_num, max_num - 1):
    print(str(my_count.increment()) + ' ', end='')
print('(' + str(max_num) + ')<-max')
