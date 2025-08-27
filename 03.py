import time
import threading
import asyncio


async def task(название, секунды):
    print(f"Начинаю {название}")
    await asyncio.sleep(секунды)  # Асинхронная пауза
    print(f"Закончил {название}")

async def main():
    start = time.time()
    await asyncio.gather(
        task("загрузка файла", 3),
        task("отправка email", 2),
        task("запись в БД", 1)
    )
    end = time.time()
    print(f"Время: {end - start} секунд")
    
asyncio.run(main())

