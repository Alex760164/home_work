"""
1. Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся записи о номере заказа,
названии книги, колличестве и стоимости одной книги, как представленно ниже, в таблице.
+--------------+--------------------------------------+----------+----------------+
| Order Number |       Book Title and Author          | Quantity | Price per Item |
+--------------+--------------------------------------+----------+----------------+
|        34587 | Learning Python, Mark Lutz           |        4 |          40.95 |
|        98762 | Programming Python, Mark Lutz        |        5 |          56.80 |
|        77226 | Head First Python, Paul Barry        |        3 |          32.95 |
|        88112 | Introduction to Python3, Bernd Klein |        3 |          24.99 |
+--------------+--------------------------------------+----------+----------------+
Напишите программу на Python, которая на вход получает список списков:
[ [34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Introduction to Python3, Bernd Klein', 3, 24.99] ]
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения цены на товары и
количества. Стоимость товара должена быть увеличена на $10, если стоимость заказа меньше $100.
Программа должна использовать lambda и map.
"""

print('БУХГАЛТЕРСКАЯ КНИГА\n\tДобавление записи в книгу')

"""
ledger = [
            [34587, 'Learning Python, Mark Lutz', 4, 40.95],
            [98762, 'Programming Python, Mark Lutz', 5, 56.80],
            [77226, 'Head First Python, Paul Barry', 3, 32.95],
            [88112, 'Introduction to Python3, Bernd Klein', 3, 24.99],
            [99999, 'Test test tes', 5, 11.11]
        ]
"""

run_stop = 'y'
ledger = []
while run_stop != 'n':
    if run_stop == 'y':
        ord_numb = int(input('\n\t\tУкажите номер книги: '))
        name_book = input('\t\tУкажите название книги и автора: ')
        quantity = int(input('\t\tУкажите количество книг: '))
        price = float(input('\t\tУкажите стоимость книги: '))
        record = [ord_numb, name_book, quantity, price]
        ledger.append(record)
        run_stop = input('\n\t\tХотите продолжить (y / n): ')
    elif run_stop == 'n':
        break
    else:
        run_stop = input('\t\tХотите продолжить (y / n): ')

print('\nОТВЕТ:\n\tВходной список:', ledger)

#list2 = list(zip(map(lambda x: x[0], ledger), map(lambda x: x[2] * x[3] if x[2] * x[3] >= 100 else x[2] * x[3] + 10, ledger)))

list2 = list(map(lambda x: (x[0], round(x[2] * x[3], 2) if round(x[2] * x[3], 2) >= 100 else round(x[2] * x[3], 2) + 10), ledger))

print('\tВыходной список', list2)
