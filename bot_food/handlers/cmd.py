from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from main import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = "/drink"
    keyboard.add(button_1)
    button_2 = "/food"
    keyboard.add(button_2)
    await message.answer(f'Привет, {message.from_user.full_name}! '
                         f'Выбирай')
