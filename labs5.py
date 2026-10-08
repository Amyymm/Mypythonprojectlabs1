
# def circle_area(radius):
#     pi = 3.14159
#     return pi * radius * radius
#
#
#
# def rectangle_area(width, height):
#     return width * height
#
#
#
# def triangle_area(base, height):
#     return base * height / 2
#
#
# def main():
#
#     figure = input("Введіть фігуру (круг, прямокутник, трикутник): ")
#
#     if figure == "круг":
#         radius = float(input("Введіть радіус: "))
#         result = circle_area(radius)
#         print("Площа круга:", result)
#
#     elif figure == "прямокутник":
#         width = float(input("Введіть ширину: "))
#         height = float(input("Введіть висоту: "))
#         result = rectangle_area(width, height)
#         print("Площа прямокутника:", result)
#
#     elif figure == "трикутник":
#         base = float(input("Введіть основу: "))
#         height = float(input("Введіть висоту: "))
#         result = triangle_area(base, height)
#         print("Площа трикутника:", result)
#
#     else:
#         print("Такої фігури немає.")
#
#
# main()



# def is_prime(n):
#
#     if n < 2:
#         return False
#
#
#     for i in range(2, n):
#
#         if n % i == 0:
#             return False
#
#     е
#     return True
#
#
#
# def divisors(n):
#     result = []
#
#
#     for i in range(1, n + 1):
#
#         if n % i == 0:
#             result.append(i)
#
#     return result
#
#
#
# def digit_sum(n):
#     total = 0
#
#
#     while n > 0:
#
#         digit = n % 10
#
#
#         total += digit
#
#
#         n = n // 10
#
#     return total
#
#
#
# def main():
#
#     n = int(input("Введіть натуральне число: "))
#
#
#     if is_prime(n):
#         print("Просте число: так")
#     else:
#         print("Просте число: ні")
#
#
#     print("Дільники:", divisors(n))
#
#
#     print("Сума цифр:", digit_sum(n))
#
#
#
# main()


def check_length(password):
    return len(password) >= 8



def has_digit(password):
    for symbol in password:
        if symbol.isdigit():
            return True

    return False



def has_uppercase(password):
    for symbol in password:
        if symbol.isupper():
            return True

    return False


def has_lowercase(password):
    for symbol in password:
        if symbol.islower():
            return True

    return False



def has_special(password):
    for symbol in password:

        if not symbol.isalnum():
            return True

    return False


def validate_password(password):

    errors = []


    if not check_length(password):
        errors.append("пароль має містити щонайменше 8 символів")


    if not has_digit(password):
        errors.append("немає цифри")


    if not has_uppercase(password):
        errors.append("немає великої літери")


    if not has_lowercase(password):
        errors.append("немає малої літери")


    if not has_special(password):
        errors.append("немає спеціального символу")


    if len(errors) == 0:
        return True, errors

    return False, errors



def main():

    password = input("Введіть пароль: ")


    valid, errors = validate_password(password)


    if valid:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        print("Не виконано:")


        for error in errors:
            print("-", error)



main()