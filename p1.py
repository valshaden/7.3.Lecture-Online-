import time
import asyncio


async def task(название, секунды):
    print(f"Начинаю {название}")
    await asyncio.sleep(секунды)  # Имитируем долгую работу
    print(f"Закончил {название}")



async def main():
    start = time.time()
    tasks = [
        asyncio.create_task(task("загрузка файла", 3)),
        asyncio.create_task(task("отправка email", 2)),
        asyncio.create_task(task("запись в БД", 1))        
    ]
    await asyncio.wait(tasks)
    
    
    end = time.time()
    print(f"Время: {end - start} секунд")
    
asyncio.run(main())

