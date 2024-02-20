from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text="📋 To'lov hisoblari")
async def bot_echo(message: types.Message):
    await message.answer('Tanlang!')

