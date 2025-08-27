import time

def task(название, секунды):
    print(f"Начинаю {название}")
    time.sleep(секунды)  # Имитируем долгую работу
    print(f"Закончил {название}")

start = time.time()
start = time.time()
task("загрузка файла", 3)
task("отправка email", 2)
task("запись в БД", 1)
end = time.time()
print(f"Время: {end - start} секунд")

