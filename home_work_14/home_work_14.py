"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей
(слева и справа) и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
import random

random_list = [random.randint(1, 100) for _ in range (15)]
print('Список чисел:', random_list)

count = 0
for i in range(1, len(random_list) - 1):
    if (random_list[i - 1] < random_list[i]) and (random_list[i] > random_list[i + 1]):
        count += 1
    i += 1
print('ОТВЕТ:\n\t Количество элементов:', count)