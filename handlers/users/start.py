from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.mainBtn import menuBtn
from keyboards.inline.inlineBnt import menejer
from sheet import *
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await checkUser(message)

async def checkUser(message):
    check = await getData1(value_to_find=message.from_user.id, cur=4, table='👥 Xodimlar')
    print(check)
    if check:
        await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=menuBtn)
    else:
        text = """
    ⚠️ Siz hali rasmiy ro’yhatdan o’tmagansiz! Iltimos, Xodimlar bo’limiga bog’laning va biz bilan hamkorlik asosida, savdolaringizni oshiring!

    📞 Aloqa uchun: (33) 090-78-49
                    """
        await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n"
                             f"{text}", reply_markup=menejer())

