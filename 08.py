import asyncio
import random


async def car(name, distance = 10):
    position = 0
    
    while position < distance:
        speed += random.uniform(0.5, 1)        
        await asyncio.sleep(speed)
        position += 1
        print(f"🚗 {name}: {'█' * position}{'░' * (distance - position)} ({position}/{distance})")
        
        print(f"{name} - {position}")

print(f"🚗 : {'█' * 5}{'░' * (10 - 5)} ({10}/{5})")