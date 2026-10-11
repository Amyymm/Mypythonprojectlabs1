# import math
#
# r = float(input("радіус: "))
# a = float(input("перший катет: "))
# b = float(input("другий катет: "))
# n = int(input("предметів: "))
# k = int(input("в упаковці: "))
#
# s = math.pi * r ** 2
# c = math.sqrt(a ** 2 + b ** 2)
# packages = math.ceil(n / k)
#
# print("площа круга:", round(s, 2))
# print("гіпотенуза:", round(c, 2))
# print("потрібно упаковок:", packages)

# import random
# import statistics
#
# n = int(input("кількість оцінок: "))
#
# if n <= 0:
#     print("кількість оцінок повинна бути додатною")
# else:
#     grades = []
#
#     for i in range(n):
#         grade = random.randint(1, 12)
#         grades.append(grade)
#
#     minimum = min(grades)
#     maximum = max(grades)
#     average = statistics.mean(grades)
#     median = statistics.median(grades)
#
#     high_grades = 0
#
#     for grade in grades:
#         if grade >= 10:
#             high_grades += 1
#
#     print("оцінки:", grades)
#     print("min:", minimum)
#     print("max:", maximum)
#     print("середнє:", round(average, 2))
#     print("медіана:", median)
#     print("оцінок 10–12:", high_grades)




#
# from datetime import date
#
# year = int(input("рік: "))
# month = int(input("місяць: "))
# day = int(input("день: "))
#
# event_date = date(year, month, day)
# today = date.today()
#
# if event_date > today:
#     difference = event_date - today
#     print("до події залишилося:", difference.days, "днів")
# elif event_date < today:
#     difference = today - event_date
#     print("після події минуло:", difference.days, "днів")
# else:
#     print("ця подія відбувається сьогодні!")


#
# import random
# import statistics
#
#
# def generate_grades(count):
#     grades = []
#
#     for i in range(count):
#         grades.append(random.randint(1, 12))
#
#     return grades
#
#
# def average_grade(grades):
#     return statistics.mean(grades)
#
#
# def get_level(average):
#     if average >= 10:
#         return "високий"
#     elif average >= 7:
#         return "достатній"
#     elif average >= 4:
#         return "середній"
#     else:
#         return "початковий"





