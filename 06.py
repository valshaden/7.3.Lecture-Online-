import requests
import time


def get_site(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except:
        return "Ошибка"


sites = [
        "https://python.org",
        "https://github.com", 
        "https://stackoverflow.com"
    ]

start = time.time()

for site in sites:
    print(f"Запрашиваем {site}")
    r = get_site(site)
    print(r)

end = time.time()
print(f"Синхронно: {end - start:.1f} секунд")

