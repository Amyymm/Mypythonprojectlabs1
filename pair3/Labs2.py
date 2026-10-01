# text = input("введіть рядок: ")
#
# # Загальна кількість символів
# print("символів:", len(text))
#
# # Кількість літер
# letters = 0
# for char in text:
#     if char.isalpha():
#         letters += 1
# print("літер:", letters)
#
# # Кількість цифр
# digits = 0
# for char in text:
#     if char.isdigit():
#         digits += 1
# print("цифр:", digits)
#
# # Кількість пробілів
# probilu = text.count(" ")
# print("пробілів:", probilu)
#
# # Кількість голосних
# golosni = "eyuioa"
# golosni_count = 0
#
# for char in text:
#     if char in golosni:
#         golosni_count += 1
#
# print("голосних:", golosni_count)
#
# # Кількість слів
# words = text.split()
# print("cлів:", len(words))




# # Вводимо прізвище, ім'я та по батькові
# text = input()
#
# # Розділяємо рядок на окремі слова
# parts = text.split()
#
# # Перевіряємо, чи отримали рівно 3 частини
# if len(parts) != 3:
#     print("помилка: потрібно ввести прізвище, ім'я та по батькові")
# else:
#     # Робимо першу літеру великою, а інші - маленькими
#     surname = parts[0].capitalize()
#     name = parts[1].capitalize()
#     po_batkovi = parts[2].capitalize()
#
#     # Формуємо запис Прізвище І.П.
#     result = surname + " " + name[0] + "." + po_batkovi[0] + "."
#
#     print(result)



# Вводимо два рядки


# text1 = input()
# text2 = input()
#
# # Прибираємо пробіли та переводимо всі літери в нижній регістр
# text1 = text1.replace(" ", "").lower()
# text2 = text2.replace(" ", "").lower()
#
# # Сортуємо символи в обох рядках
# sorted_text1 = sorted(text1)
# sorted_text2 = sorted(text2)
#
# # Порівнюємо рядки
# if sorted_text1 == sorted_text2:
#     print("рядки є анаграмами.")
# else:
#     print("рядки не є анаграмами.")
#
# # Виводимо нормалізовані рядки
# print("нормалізований перший рядок:", text1)
# print("нормаізований другий рядок:", text2)


#
#
# sentence = input()
#
# words = sentence.split()
#
# # довжина найдовшого слова
# max_length = max(len(word) for word in words)
#
# # довжина найкоротшого слова
# min_length = min(len(word) for word in words)
#
# #  всі найдовші слова
# longest = []
#
# for word in words:
#     if len(word) == max_length and word not in longest:
#         longest.append(word)
#
# # Звсі найкоротші слова
# shortest = []
#
# for word in words:
#     if len(word) == min_length and word not in shortest:
#         shortest.append(word)
#
# #  унікальні слова без урахування регістру
# unique_words = set()
#
# for word in words:
#     unique_words.add(word.lower())
#
# print("найдовші:", ", ".join(longest))
# print("найкоротші:", ", ".join(shortest))
# print("унікальних слів:", len(unique_words))
#
# #  слово, яке потрібно замінити
# old_word = input()
#
# #  нове слово
# new_word = input()
#
#
# for i in range(len(words)):
#     if words[i].lower() == old_word.lower():
#         words[i] = new_word
#
#
# result = " ".join(words)
#
# print("після заміни:", result)