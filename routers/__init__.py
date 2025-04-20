from aiogram import Dispatcher
from .menu import menu_router

def register_routers(dp: Dispatcher):
    dp.include_router(menu_router)