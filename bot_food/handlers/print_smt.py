from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class Print_smt_cl(StatesGroup):
    waiting_print = State()


async def print_smt_start(message: types.Message):
    await message.answer("Что вы хотите сделать?", reply_markup=types.ReplyKeyboardRemove())
    await Print_smt_cl.waiting_print.set()


async def print_smt_f(message: types.Message, state: FSMContext):
    if 'кот' in message.text:
        await message.reply('НИКАКИХ КОТОВ')
    else:
        await message.answer('okeeeeey')
    await state.finish()


def register_handlers_print_smt(dp: Dispatcher):
    dp.register_message_handler(print_smt_start, commands="something", state="*")
    dp.register_message_handler(print_smt_f, state=Print_smt_cl.waiting_print)
