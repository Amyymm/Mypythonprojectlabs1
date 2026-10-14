# with open('text.txt', 'r', encoding="utf-8") as file:
#     text = file.read()
#
# lines = text.splitlines()
# words = text.split()
#
# print("пядків:", len(lines))
# print("слів:", len(words))
# print("символів:", len(text))
#
# if lines:
#     longest_line = max(lines, key=len)
#     number = lines.index(longest_line) + 1
#
# print("найдовший рядок: No", number, ", ", len(longest_line), "символів", sep="")
# print("текст:", longest_line)



# fragment = input("Фрагмент: ")
#
# with open("text.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#
# found = False
#
# for i in range(len(lines)):
# if fragment.lower() in lines[i].lower():
# print(f"{i + 1}: {lines[i].strip()}")
#         found = True
#
# if not found:
# print("Збігів не знайдено")



# fragment = input("Введіть фрагмент тексту: ")
# with open('text.txt', 'r', encoding="utf-8") as file:
#     lines = file.readlines()
# found = False
# for i in range(len(lines)):
#     if fragment.lower() in lines[i].lower():
#         print(i + 1, ":", lines[i].strip())
#         found = True
# if not found:
#     print("збігів не знайдено")




student = {}
with open("grdes.csv", "r", encoding = "utf-8") as file:
    for line in file:
        name, subject, grade = line.split()(";")
        grade = float(grade)
        if name not in student:
            student[name] = []
            student[name].append(grade)


            def average_grade(grades):
                return sum(grades) / len(grades)


            results = []

            for name in students:
                grades = students[name]
                average = average_grade(grades)

                results.append((name, len(grades), average))
                results.sort(key=lambda x: x[2], reverse=True)
                results.sort(key=lambda x: x[2], reverse=True)
                best_students = []
                for name, count, average in results:
                    if average == best_average:
                        best_students.append(name)

                        with open("report.txt", "w", encoding="utf-8") as file:
                            for name, count, average in results:
                                file.write(f"{name} — оцінок: {count} — середній: {average:.2f}\n")

                                file.write(
                                    f"Найкращий результат: {' та '.join(best_students)} — {best_average:.2f}"
                                )






