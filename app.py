import tkinter as tk
from tkinter import messagebox

count = 0
root = tk.Tk()

def view(count,labelText,buttonTextw):
    if count == 0:
        label = tk.Label(root, text = labelText)
        label.pack(pady=10)

        count += 1
        button = tk.Button(root, text="Пройти тест", command=check_input(buttonTextw,count), font=("Arial", 11, "bold"), bg="lightgreen" )
        button.pack(pady=15)

def check_input(ansver, count):
    if count == 0:
        count += 1
        view(count, "1")
    if count == 1 and ansver == "первый ответ":
        count += 1
        view(count,"2")


root.title("Дух расстроенного рояля. Тест")
root.geometry("600x300")

root.mainloop()  