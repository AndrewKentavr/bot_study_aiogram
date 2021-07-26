import asyncio

from random import randint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand

from config import BOT_TOKEN, ADMINS
import logging

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    await set_commands(bot)
    await bot.send_message(ADMINS, "Bot - on", reply_markup=types.ReplyKeyboardRemove())


async def on_shutdown(dp):
    await bot.send_message(ADMINS, "Bot - Off", reply_markup=types.ReplyKeyboardRemove())
    # await bot.close()
    # await storage.close()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/drinks", description="Заказать напитки"),
        BotCommand(command="/food", description="Заказать блюда"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
