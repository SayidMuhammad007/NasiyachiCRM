from aiogram import types

from keyboards.inline.inlineBnt import HR
from loader import dp


# Echo bot
@dp.message_handler(text="🚻 HR bo’limi")
async def bot_echo(message: types.Message):
    await message.answer("Kerakli bo`limni tanlang!", reply_markup=HR())
