import time
import aiohttp, asyncio


async def get_site(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                return response.status
    except:
        print(f"Ошибка: {url}")


sites = [
        "https://github.com", 
        "https://python.org",
        "https://stackoverflow.com"
    ]

async def main():

    start = time.time()
    results = await asyncio.gather(*[get_site(site) for site in sites])


    end = time.time()
    print(f"Синхронно: {end - start:.1f} секунд")

asyncio.run(main())