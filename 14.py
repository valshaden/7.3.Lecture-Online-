import asyncio
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Гонки машин")

# Глобальные переменные для состояния гонок
race_data = {
    "cars": ["Красная", "Синяя", "Зеленая"],
    "positions": [0, 0, 0],
    "distance": 10,
    "racing": False,
    "winner": None
}


@app.get("/", response_class=HTMLResponse)
def home():
    return open("PRACTICE\lesson-18\index.html", "r", encoding="utf-8").read()


async def car_race(car_index):

    while race_data["positions"][car_index] < race_data["distance"] and race_data["racing"]:
        # Случайная скорость
        await asyncio.sleep(random.uniform(0.5, 1.5))
        race_data["positions"][car_index] += 1
       

@app.get("/start")
async def start_race():
    """Запускает гонки"""
    if race_data["racing"]:
        return {"message": "Гонки уже идут!"}
    
    # Сбрасываем состояние
    race_data["positions"] = [0, 0, 0]
    race_data["racing"] = True
    race_data["winner"] = None
    
    # Запускаем машины асинхронно
    tasks = [car_race(i) for i in range(3)]
    asyncio.create_task(asyncio.gather(*tasks))
    
    return {"message": "🏁 Гонки начались!"}
    

@app.get("/status")
def get_status():
    """Возвращает текущее состояние гонок"""
    return {
        "cars": race_data["cars"],
        "positions": race_data["positions"],
        "distance": race_data["distance"],
        "racing": race_data["racing"],
        "winner": race_data["winner"]
    }


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)
