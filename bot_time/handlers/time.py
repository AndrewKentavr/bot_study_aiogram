from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from asyncio import sleep as async_sleep


class TimeBox(StatesGroup):
    time = State()


async def time_start(message: types.Message):
    await message.answer("Введите время:", reply_markup=types.ReplyKeyboardRemove())
    await TimeBox.time.set()


async def time(message: types.Message, state: FSMContext):
    time_sec = int(message.text)
    await state.update_data(chosen_time=time_sec)
    await message.answer(f'Время пошло: {time_sec}')
    await async_sleep(time_sec)
    await message.answer('ТАЙМЕР')
    await state.finish()


def register_handlers_time(dp: Dispatcher):
    dp.register_message_handler(time_start, commands='time', state="*")
    dp.register_message_handler(time, state=TimeBox.time)
