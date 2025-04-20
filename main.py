from contextlib import asynccontextmanager
import os
import uvicorn
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from fastapi import FastAPI
from routers import register_routers
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
TOKEN = os.getenv("BOT_TOKEN")

@asynccontextmanager
async def lifespan(app: FastAPI):
    register_routers(dp)
    webhook_info = await bot.get_webhook_info()
    if webhook_info != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL, drop_pending_updates=True)
    logging.info("App started")
    yield
    await bot.session.close()
    logging.info("App stopped")

app = FastAPI(lifespan=lifespan)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@app.post("/webhook")
async def webhook(data: dict) -> None:
    try:
        update = Update(**data)
        await dp.feed_update(
            bot=bot,
            update=update
        )
    except Exception as e:
        logging.error(e, exc_info=True)
        
        
def main():
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
    
if __name__ == "__main__":
    main()