import asyncio
import random
from aiogram import Router
from aiogram.types import Message


menu_router = Router()


@menu_router.message()
async def start(message: Message):
    await message.answer("<b>привет</b>", parse_mode="HTML")
            
