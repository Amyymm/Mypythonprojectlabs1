# Завдання №1
# import math
# radius = float(input("введіть радіус:"))
# a = float(input("ведіть перший катет:"))
# b = float(input("ведіть другий катет:"))
# n = int(input("ведіть кількість предметів:"))
# k = int(input("ведіть кількість предметів в упаковці:"))
# area = math.pi * radius ** 2
# gipotenyz = math.sqrt(a ** 2 + b ** 2)
# packages = math.ceil(n / k)
#
#
#
#
#
# print("площа круга:", round(area, 2))
# print("ніпотенуза:", round(gipotenyz, 2))
# print("потрібно упаковок:", packages)

# Завдання №3

#
# from datetime import date
#
# year = int(input("ведіть рік: "))
# month = int(input("введіть місяць: "))
# day = int(input("ведіть день: "))
# event = date(year, month, day)
# today = date.today()
# if event > today:
#     difference = event - today
#     print("до події залишилося:", difference.days, "днів")
# elif event < today:
#     difference = today - event
#     print("від події минуло:", difference.days, "днів")
# else:
#     print("подія відбаається сьогодні!")


# Завдання №4


import random
import statistics

def generate_grades(count):
    grades = []
    for i in range(count):
        grades.append(random.randint(1, 12))
        return grades

def average_grade(grades):
    return statistics.mean(grades)
def get_level(average):
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатеій"
    elif average >= 4:
        return "середній"
    else:
        return "початковий"







