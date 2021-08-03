from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart
from asyncio import sleep as async_sleep


async def book_send(message: types.Message):
    await message.answer('Отправляю бота:')
    for i in range(3):
        await async_sleep(i + 1)
        await message.answer(str(3 - i))
    await message.answer_document(open('C:/Users/andrt/PycharmProjects/bot_study_aiogram/bot_book/Evgeni_Onegin.pdf', 'rb'))


def register_handlers_book(dp: Dispatcher):
    dp.register_message_handler(book_send, commands='book', state='*')
