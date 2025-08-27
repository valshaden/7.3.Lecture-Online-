import asyncio
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Гонки машин")

@app.get("/")
def home():
    return {'ок': "ok"}

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