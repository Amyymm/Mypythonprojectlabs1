# name = input("Enter your name: ")


#
#
# print("Створення файлу")
#
# with open ("hello.txt" , "w", encoding="utf-8") as file:
#     file.write ("Аня обіцяє вчитися!\n")
#
#
# r-  файл читання
# w- щапис,якшщо файл вже існує то вміст стерається і нове записується
# a - створює файл,старий вміст не витирається , ставить в кінець
# x - створення нового файлу,але якшо такий файл вже існцє то буде помилка




#

# import os
#
# with open('text.txt', 'r', encoding="utf-8") as file:
#     text = file.read()
# print(text)
#
# with open('log.txt', 'w', encoding="utf-8") as file:
#     file.write(" Перший запуск\n ")
# with open(' log.txt', 'w', encoding="utf-8") as file:
#     file.write("Другий запуск,перший видаленно\n ")
# with open(' log.txt', 'a', encoding="utf-8") as file:
#     file.write("Новий запис,додаємо у кінець\n ")
# with open(' log.txt', 'r', encoding="utf-8") as file:
#     print(file.read())

#Способи читання