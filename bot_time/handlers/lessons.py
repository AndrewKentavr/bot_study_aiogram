from aiogram import types, Dispatcher


async def lesson_start(message: types.Message):
    await message.answer(
        '''Приятно, граждане, наблюдать, как стремящиеся вытеснить традиционное производство, нанотехнологии освещают
         чрезвычайно интересные особенности картины в целом, однако конкретные
          выводы, разумеется, описаны максимально подробно. Сложно сказать,
           почему сделанные на базе интернет-аналитики''')


def register_handlers_lesson(dp: Dispatcher):
    dp.register_message_handler(lesson_start, commands='lesson', state="*")
