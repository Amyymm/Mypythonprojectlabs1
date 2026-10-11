#Завдання№4
# import tkinter as tk
# import student_utils
#
# students = ["Анна", "Іван", "Ольга"]
#
#
# def create_report():
#     count = entry.get()
#
#     if not count.isdigit():
#         result.delete("1.0", tk.END)
#         result.insert(tk.END, "введіть число від 1 до 20")
#         return
#
#     count = int(count)
#
#     if count < 1 or count > 20:
#         result.delete("1.0", tk.END)
#         result.insert(tk.END, "введіть число від 1 до 20")
#         return
#
#     report = ""
#
#     for name in students:
#         grades = student_utils.generate_grades(count)
#         average = student_utils.average_grade(grades)
#         level = student_utils.get_level(average)
#
#         report += name + "\n"
#         report += "оцінки: " + str(grades) + "\n"
#         report += "середній бал: " + str(round(average, 2)) + "\n"
#         report += "рівень: " + level + "\n\n"
#
#     print(report)
#     result.delete("1.0", tk.END)
#     result.insert(tk.END, report)
#
#
# window = tk.Tk()
# window.title("статистика учнів")
# window.geometry("400x400")
# window.configure(bg="#F4C7A1")
#
# label = tk.Label(
#     window,
#     text="кількість оцінок (1–20):",
#     bg="#F4C7A1",
#     fg="#59321F"
# )
# label.pack(pady=5)
#
# entry = tk.Entry(window)
# entry.pack(pady=5)
#
# button = tk.Button(
#     window,
#     text="сформувати звіт",
#     command=create_report,
#     bg="#A64B24",
#     fg="white",
#     activebackground="#803719",
#     activeforeground="white"
# )
# button.pack(pady=10)
#
# result = tk.Text(
#     window,
#     width=45,
#     height=15,
#     bg="#FFF0E3",
#     fg="#59321F"
# )
# result.pack(pady=5)
#
# window.mainloop()



























