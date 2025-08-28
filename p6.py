import tkinter as tk
import time
import random
import threading

car_labels = {}

root = tk.Tk()
root.title("Гонки")
root.geometry("400x200")

# Заголовок
tk.Label(root, text="🏁 ГОНКИ 🏁", font=("Arial", 14)).pack(pady=10)

# Кнопки
button_frame = tk.Frame(root)
button_frame.pack()


def car_race(name):
    position = 0    # Начальная позиция
    distance = 10
    
    while position < distance:
        # Случайная пауза = разная скорость машин
        time.sleep(random.uniform(0.5, 1.5))
        position += 1  # Машина продвигается 
        progress = "🚗" + "█" * position + "░" * (distance - position)
        root.after(0, lambda p=progress, n=name: car_labels[n].config(text=f"{n}: {p}"))


def start_race():
    cars = ["Красная", "Синяя", "Зеленая"]
    
    for name in cars:
        thread = threading.Thread(target=car_race, args=(name,))
        thread.start()  
    
    

tk.Button(button_frame, text="СТАРТ", command=start_race, 
         bg="green", fg="white", width=8).pack(side=tk.LEFT, padx=5)

tk.Button(button_frame, text="СБРОС", command=..., 
         bg="red", fg="white", width=8).pack(side=tk.LEFT, padx=5)

# Машины

car_labels = {}
for name, color in [("Красная", "red"), ("Синяя", "blue"), ("Зеленая", "green")]:
    label = tk.Label(root, text=f"{name}: Ждет старта", 
                    font=("Courier", 10), fg=color)
    label.pack(pady=5)
    car_labels[name] = label
    


root.mainloop()