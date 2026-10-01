# name = "Ann"
# city = "Kyiv"
# messege = "hello world"
#
#
#
# print(len(messege)) #- ПОВЕРТАЄ КІЛЬКІСТЬ СИМВОЛІВ!
#
# print(name[0]) #- перший елемент слова (Ann)
# print(name[-1]) # - останній елемент слова (Ann)
# print(messege[len(messege)-1])
# print(city[10]) # - помилка

# text = input()
# print(text[0])
# if len(text) >0:
#     print(text[0])
# else:
#     print("Рядок порожній")
#
# text = "hello world"
# print(text[:2])
# print(text[2:])
# print(text[2:5])
# print(text[::2])
# print(text[::-1])#- в зворотньому порядку
#
# text = "       Python     programing     "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())


# login = "admin"
# user_login = input("Enter your login username: : ")
# if user_login.strip().lower() == login:
#     print("Welcome admin!")


# text = "Python"
# for i in text:
#     print(char)


# isdigit - перевіряє чи складається строка з цифр!!!!!!!

# password = "123qwerty123"
# # print(password.isdigit())
# digits = 0
# letters = 0
#
# for i in password:
#     if i.isdigit():
#         digits += 1
# print(f"цифр": {digits},"літер: {letters})
#
#
# print(password.isalpha()) #-тільки літери
# print(password.isdigit()) #- тільки цифри
# print(password.isalnum()) #-літерпи або цифри


# text = input("введіть речення:" ).strip().lower()
# golosni = "аеєиіїуоюя"
#
# counter_golosni = 0
# for i in text:
#     if i in golosni:
#         counter_golosni += 1
# print(counter_golosni)

#
# text = "привіт світ"
# words = text.split()
# print(words)
#
# text_new = " ".join(words)
# print(text_new)
#



# text = "Python is easy to learn"
# new_text = text.replace("Python","Javascript")
# print(new_text)
#
# word = "дід"
# word_norm = word.strit().lower()
# if word_norm == word_norm[::-1]:
#     print("паліндром")
# else:
#     print("не паліндром")

# text = "hello world"
#
# print(text.find("o"))
# print(text.count("l"))


# emeil = "anna.rykova2011@gmail.com"
# if emeil.lower().endswith("@gmail.com"): #startswith
#     print("у тебе гугівська пошта")
