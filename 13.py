import asyncio
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Гонки машин")

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html", "r", encoding="utf-8").read()

race_data = {
    "cars": ["Красная", "Синяя", "Зеленая"],
    "positions": [0, 0, 0],
    "distance": 10,
    "racing": False,
    "winner": None
}


async def car_race(car_index, distance = 10):    
    while race_data["position"][car_index] < distance:
        speed = random.uniform(0.5, 2)        
        await asyncio.sleep(speed)
        race_data["positions"][car_index] += 1
       

@app.get("/start")
async def start():    
    race_data["positions"] = [0, 0, 0]
    race_data["racing"] = True
    race_data["winner"] = None
    
    tasks = [car_race(i) for i in range(3)]
    asyncio.create_task(asyncio.gather(*tasks))
    
        
    return {"message": "🏁 Гонки начались!"}
    

if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)
    

async def car(name, distance = 10):
    position = 0
    
    while position < distance:
        speed = random.uniform(0.5, 2)        
        await asyncio.sleep(speed)
        position += 1
        print(f"🚗 {name}: {'█' * position}{'░' * (distance - position)} ({position}/{distance})")
        
    print(f"🏆 {name} финишировала!")    
    return name

async def race():
    
    tasks = [
        asyncio.create_task(car("🚗1")),
        asyncio.create_task(car("🚗2")),
        asyncio.create_task(car("🚗3"))
    ]
    await asyncio.gather(*tasks)
    

# asyncio.run(race())