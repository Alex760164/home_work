"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей
(слева и справа) и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
import random
random_list = [random.randint(1, 100) for _ in range(15)]
print('Список чисел:', random_list)

# 1-й способ (for)
count = 0
for i in range(1, len(random_list) - 1):
    if (random_list[i - 1] < random_list[i]) and (random_list[i] > random_list[i + 1]):
        count += 1
    i += 1
print('ОТВЕТ:\n\t1-й способ (for): Количество элементов:', count)

# 2-й способ (while)
count_2 = 0
j = 1
while j < len(random_list)-1:
    if (random_list[j - 1] < random_list[j]) and (random_list[j] > random_list[j + 1]):
        count_2 += 1
    j += 1
print('\t2-й способ (while): Количество элементов:', count_2)