import asyncio
import random


async def car(name, distance = 10):
    position = 0
    
    while position < distance:
        speed = random.uniform(0.5, 2)        
        await asyncio.sleep(speed)
        position += 1
        print(f"🚗 {name}: {'█' * position}{'░' * (distance - position)} ({position}/{distance})")
        
      


async def race():
    
    tasks = [
        asyncio.create_task(car("🚗1")),
        asyncio.create_task(car("🚗2")),
        asyncio.create_task(car("🚗3"))
    ]
    await asyncio.gather(*tasks)
    

asyncio.run(race())

