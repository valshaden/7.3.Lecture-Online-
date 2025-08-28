import tkinter as tk
import time
import random
root = tk.Tk()
root.title("Гонки")
root.geometry("400x200")
# Заголовок
tk.Label(root, text="🏁 ГОНКИ 🏁", font=("Arial", 14)).pack(pady=10)
# Кнопки
button_frame = tk.Frame(root)
button_frame.pack()
tk.Button(button_frame, text="СТАРТ", command=..., 
         bg="green", fg="white", width=8).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="СБРОС", command=..., 
         bg="red", fg="white", width=8).pack(side=tk.LEFT, padx=5)
root.mainloop()
