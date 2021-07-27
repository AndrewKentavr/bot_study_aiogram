import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from bot_time.handlers.register_cmd import reg_cmd, register_handlers_time, register_handlers_lesson

from config import BOT_TOKEN, ADMINS
import logging

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    await set_commands(bot)
    reg_cmd(dp)  # функция регистрации "register_message_handler"
    await bot.send_message(ADMINS, "Bot - on", reply_markup=types.ReplyKeyboardRemove())


async def on_shutdown(dp):
    await bot.send_message(ADMINS, "Bot - Off", reply_markup=types.ReplyKeyboardRemove())
    # await bot.close()
    # await storage.close()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Просмотр функционала"),
        BotCommand(command="/time", description="Засечь время"),
        BotCommand(command="/lesson", description="Посмотреть уроки")
    ]
    await bot.set_my_commands(commands)


# async def asc_main():
#     tasks = [
#         register_handlers_time(dp),
#         register_handlers_lesson(dp)
#     ]
#     await asyncio.gather(*tasks)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    # asyncio.run(asc_main())
