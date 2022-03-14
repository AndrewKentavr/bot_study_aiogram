from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart


async def bot_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = ["/book"]
    keyboard.add(*button_1)
    await message.answer(f'Привет, {message.from_user.full_name}! '
                         f'Посмотри на это:', reply_markup=keyboard)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
