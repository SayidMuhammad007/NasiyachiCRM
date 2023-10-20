from aiogram import types

from keyboards.default.mainBtn import partnerMenu
from loader import dp


# Echo bot
@dp.message_handler(text="🤝 Hamkorlar bo’limi")
async def bot_echo(message: types.Message):
    await message.answer(text='Istalgan holatdagi hamkorni tanlang!', reply_markup=partnerMenu)
