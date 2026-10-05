# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
#
# positive = []
# negative = []
# even = []
# multiple_3 = []
#
#
# for number in numbers:
#
#
#     if number > 0:
#         positive.append(number)
#
#
#     if number < 0:
#         negative.append(number)
#
#
#     if number % 2 == 0:
#         even.append(number)
#
#
#     if number % 3 == 0:
#         multiple_3.append(number)
#
#
#
# minimum = min(numbers)
# maximum = max(numbers)
# total = sum(numbers)
# average = total / len(numbers)
#
#
#
#
# print("додатні:", positive)
# print("від’ємні:", negative)
# print("парні:", even)
# print("кратні 3:", multiple_3)
#
# print("min:", minimum)
# print("max:", maximum)
# print("sum:", total)
# print("average:", round(average, 2))
#/////////




#
# group1 = {'Anna', 'Ivan', 'Olha'}
# group2 = {'Ivan', 'Maksym', 'Olha'}
#
#
# common = group1 & group2
#
#
# only_group1 = group1 - group2
#
#
# only_group2 = group2 - group1
#
#
# all_participants = group1 | group2
#
#
# print("спільні:", ", ".join(sorted(common)))
# print("тільки group1:", ", ".join(sorted(only_group1)))
# print("тільки group2:", ", ".join(sorted(only_group2)))
# print("усі:", ", ".join(sorted(all_participants)))
#///////


# products = {
#     "milk": 48,
#     "bread": 30,
#     "tea": 75,
#     "coffee": 120,
#     "juice": 90
# }
#
#
# name = input("Введіть назву товару: ")
# price = int(input("Введіть ціну товару: "))
#
# products[name] = price
#
#
# search_name = input("Введіть товар для пошуку: ")
#
# found_price = products.get(search_name)
#
# if found_price is not None:
#     print(search_name, "—", found_price, "грн")
# else:
#     print("Товар не знайдено")
#
#
# min_price = int(input("Мінімальна ціна: "))
# max_price = int(input("Максимальна ціна: "))
#
# print("Товари в заданому діапазоні:")
#
#
# for name, price in products.items():
#     if min_price <= price <= max_price:
#         print(name, "—", price, "грн")
#////////

#
# group_info = ('10-IT', '2026/2027')
#
#
# students = {
#     'Anna': [10, 11, 12, 9, 10],
#     'Ivan': [8, 9, 10, 11, 9]
# }
#
#
# def add_student():
#     name = input("Введіть ПІБ учня: ")
#
#
#     grades = list(map(int, input("Введіть 5 оцінок через пробіл: ").split()))
#
#
#     if len(grades) != 5:
#         print("Помилка: потрібно ввести рівно 5 оцінок.")
#         return
#
#
#     for grade in grades:
#         if grade < 1 or grade > 12:
#             print("Помилка: оцінки повинні бути від 1 до 12.")
#             return
#
#     students[name] = grades
#     print("Учня додано!")
#
#
# def print_journal():
#     print(group_info[0], "—", group_info[1])
#
#     for name, grades in students.items():
#         print(name, "—", grades)
#
#
# def print_averages():
#     print("Середні бали:")
#
#     for name, grades in students.items():
#         average = sum(grades) / len(grades)
#         print(name, "—", round(average, 1))
#
#
#
# def print_rating():
#
#     rating = []
#
#     for name, grades in students.items():
#         average = sum(grades) / len(grades)
#         rating.append([name, average])
#
#
#     rating.sort(key=lambda x: x[1], reverse=True)
#
#     print("Рейтинг:")
#
#     for name, average in rating:
#         print(name, "—", round(average, 1))
#
#
# def find_best():
#     best_name = ""
#     best_average = 0
#
#     for name, grades in students.items():
#         average = sum(grades) / len(grades)
#
#         if average > best_average:
#             best_average = average
#             best_name = name
#
#     print("Найкращий результат:",
#           best_name, "—", round(best_average, 1))
#
#
#
# print_journal()
# print_averages()
# print_rating()
# find_best()
