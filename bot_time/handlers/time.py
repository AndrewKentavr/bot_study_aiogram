from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from asyncio import sleep as async_sleep


async def time_start(message: types.Message):
    await message.answer("Введите время:", reply_markup=types.ReplyKeyboardRemove())
    await TimeBox.time_ask.set()


async def time_ask(message: types.Message, state: FSMContext):
    if message.text != '5':
        print('ГЕЙ')
        await message.answer(f'ГЕЙ')
    else:
        time_sec = int(message.text)
        await state.update_data(chosen_time=time_sec)
        await message.answer(f'Время пошло: {time_sec}')
        await time(time_sec)
        # await TimeBox.next()
        await message.answer('ТАЙМЕР')
        await state.finish()


async def time(time_sec):
    print('БВМДЛВОДМЛОВМДЫТВОМТВЫЛТМДЫТВМ')
    # user_data = await state.get_data()
    # await async_sleep(user_data['chosen_time'])
    await async_sleep(time_sec)


# async def end(message: types.Message, state: FSMContext):
#     await message.answer('ТАЙМЕР')
#     await state.finish()


class TimeBox(StatesGroup):
    time_ask = State()
    # end = State()


def register_handlers_time(dp: Dispatcher):
    dp.register_message_handler(time_start, commands='time', state="*")
    dp.register_message_handler(time_ask, state=TimeBox.time_ask)
    # dp.register_message_handler(end, state=TimeBox.end)
