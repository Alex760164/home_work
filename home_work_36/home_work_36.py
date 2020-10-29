"""
Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов `Student`
также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.
Наследование здесь не понадобится.
"""


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def information_of_student(self):
        format_print = '| {fio:<30}|{age:^10}|  {grades:^48}|'
        return format_print.format(fio=self.name, age=str(self.age), grades=self.grades)


class Group:

    def __init__(self):
        self.list = []

    def add_record(self, name, age, grades):
        self.list.append(Student(name, age, grades).information_of_student())

    def print_of_screen(self):
        print('\n'.join(item for item in self.list))


src = open('src.txt', 'r', encoding='utf-8')
name_cols = '| {fio:^30}|{age:^10}|{grades:^50}|'
my_group = Group()
while True:
    data = src.readline()
    if data:
        tmp_list = data.strip('\n').split()
        point = ''.join(map(lambda x: str(x) + 3 * ' ' if x < 10 else str(x) + 2 * ' ', list(map(int, tmp_list[3:]))))
        my_group.add_record(tmp_list[1] + ' ' + tmp_list[0], tmp_list[2], point)
    else:
        break
print('+' + '-' * 93 + '+')
print(name_cols.format(fio='ФИО студента', age='Возраст', grades='Оценки'))
print('+' + '-' * 93 + '+')
my_group.print_of_screen()
print('+' + '-' * 93 + '+')
src.close()
