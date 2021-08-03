from aiogram import types, Dispatcher


async def lesson_start(message: types.Message):
    await message.answer()


def register_handlers_lesson(dp: Dispatcher):
    dp.register_message_handler(lesson_start, commands='lesson', state="*")
