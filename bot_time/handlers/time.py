from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from asyncio import sleep as async_sleep
from aiogram.dispatcher.filters import Text

from aiogram.utils.callback_data import CallbackData

callback_actions = CallbackData("fabnum", "action")


def get_keyboard_start():
    buttons = [
        'Таймер секунд',
        'Таймер минут',
        'Произвольное время'
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def time_start_func(message: types.Message):
    await message.answer("Выберите Таймер:", reply_markup=get_keyboard_start())


async def time_sec_func(message: types.Message):
    await message.reply("говно", reply_markup=types.ReplyKeyboardRemove())
    await TimeBox.time_sec_input_func.set()


async def time_sec_input_func(message: types.Message, state: FSMContext):
    try:
        time_input = int(message.text)
    except ValueError:
        await message.answer(f'Неправильные знаки')
    else:
        # await state.update_data(chosen_time=time_input)
        await message.answer('Таймер запущен')
        await async_sleep(time_input)
        await message.answer('ТАЙМЕР ТАЙМЕР')
        await state.finish()


class TimeBox(StatesGroup):
    time_sec_input_func = State()


def register_handlers_time(dp: Dispatcher):
    dp.register_message_handler(time_start_func, commands='time', state="*")
    dp.register_message_handler(time_sec_func,
                                lambda message: message.text == "Таймер секунд" or message.text == '/time_sec')
    dp.register_message_handler(time_sec_input_func, state=TimeBox.time_sec_input_func)
