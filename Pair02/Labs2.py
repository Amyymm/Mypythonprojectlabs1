# ЗАВДАННЯ 1
#
# n = int(input("введіть N: "))
#
# total = 0
# count = 0
#
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
#         count += 1
#
# print("кілкість:", count)
# print("сума:", total)
#
# if count > 0:
#     average = round(total / count, 2)
#     print("середнє:", average)
# else:
#     print("таких чисел немає.")
#


# \\\\\\\



# ЗАВДАННЯ 2

# n = int(input("введіть N: "))
#
# if n == 0:
#     count = 1
#     total = 0
#     max_digit = 0
#     min_digit = 0
# else:
#     count = 0
#     total = 0
#     max_digit = 0
#     min_digit = 9
#
#     while n > 0:
#         digit = n % 10
#         total += digit
#         count += 1
#
#         if digit > max_digit:
#             max_digit = digit
#
#         if digit < min_digit:
#             min_digit = digit
#
#         n //= 10
#
# print("кількість цифр:", count)
# print("сума цифр:", total)
# print("найбільша цифра:", max_digit)
# print("найменша цифра:", min_digit)

# ////////
# #N = int(input("Введіть N: "))
#
# for number in range(1, N + 1):
#     temp = number
#     good = True
#
#     while temp > 0:
#         digit = temp % 10
#
#         if digit != 0:
#             if number % digit != 0:
#                 good = False
#                 break
#
#         temp = temp // 10
#
#     if good:
#         print(number, end=" ")
# /////


# ЗАВДАННЯ 4
#
# width = int(input("ввведіть ширину: "))
# height = int(input("введіть висоту: "))
# border = input("введіть символ контуру: ")
# inside = input("введіть символ всередині: ")
#
# if width < 3 or height < 3:
#     print("помилка: ширина та виста повинні бути не менше 3.")
# else:
#     for row in range(height):
#         for col in range(width):
#             if (
#                 row == 0
#                 or row == height - 1
#                 or col == 0
#                 or col == width - 1
#             ):
#                 print(border, end="")
#             else:
#                 print(inside, end="")
#         print()




