import tkinter as tk
from tkinter import messagebox

# 1. Глобальная переменная для отслеживания шагов
count = 0 

root = tk.Tk()
root.title("Дух расстроенного рояля. Тест")
root.geometry("600x350") # Немного увеличили высоту, чтобы умещались радиокнопки

# Переменная Tkinter для хранения выбранного значения радиокнопки
selected_option = tk.StringVar()
answers = 0
# Хранилище для виджетов, чтобы удалять старые при смене шагов
current_widgets = []

def clear_widgets():
    """Очищает экран от старых виджетов перед загрузкой нового шага"""
    global current_widgets
    for widget in current_widgets:
        widget.destroy()
    current_widgets.clear()

def view(labelText, options):

    global current_widgets
    clear_widgets()
    
    selected_option.set("")
    
    label = tk.Label(root, text=labelText, font=("Arial", 13), wraplength=550, justify="center")
    label.pack(pady=20)
    current_widgets.append(label)
    
    # Создаем радиокнопки для каждого варианта ответа
    for option_text in options:
        rb = tk.Radiobutton(
            root, 
            text=option_text, 
            variable=selected_option, 
            value=option_text, 
            font=("Arial", 11)
        )
        rb.pack(anchor="w", padx=50, pady=5)
        current_widgets.append(rb)
        
    # Создаем кнопку подтверждения выбора
    button = tk.Button(
        root, 
        text="Далее", 
        command=check_input, 
        font=("Arial", 11, "bold"), 
        bg="lightgreen",
        width=15
    )
    button.pack(pady=20)
    current_widgets.append(button)

def check_input():
    global count
    global answers
    
    user_choice = selected_option.get()
    
    if not user_choice and count > 0:
        messagebox.showwarning("Внимание", "Пожалуйста, выберите один из вариантов!")
        return

    if count == 0:
        count += 1
        view(
            "В каком городе жил Дэвид Биккенсон?", 
            ["A) Лондон", "B) Чикаго", "С) Нью-Йорк", "D) Лос-Анджелес"]
        )
        
    elif count == 1:
        if user_choice == "B) Чикаго":
            answers += 1
        count += 1
        view("Как познакомились Хильда и Дэвид?", ["A) Они сидели в джаз-клубе в одиночестве", "B) Были знакомы давно", "C) Ждали такси под дождем", "D) Вышли на балкон и курили"])   
           
            
    elif count == 2:
        if user_choice == "D) Вышли на балкон и курили":
            answers += 1
        count += 1
        view("Какие у Дэвида отношения с родителями?", ["А) У них доверительные отношения", "B) Он не держит с ними контакта", "C) Он враждует с ними", "D) Старается избегать их"]) 
   
    elif count == 3: 
        if user_choice == "D) Старается избегать их":
            answers += 1
        count += 1  
        
        
    


view("Добро пожаловать в текстовый квест-тест!", [])

root.mainloop()
