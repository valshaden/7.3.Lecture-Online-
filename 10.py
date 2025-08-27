import asyncio
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI(title="Гонки машин")
@app.get("/", response_class=HTMLResponse)
def home():
    return {'ок': "ok"}
if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)

