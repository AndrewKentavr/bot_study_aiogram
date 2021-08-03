from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


async def cart_func(message: types.Message):
    await message.answer('ТАНЯ УЙДИТЕ')


def register_handlers_cart(dp: Dispatcher):
    dp.register_message_handler(cart_func, Text(equals=".-."), state="*")
