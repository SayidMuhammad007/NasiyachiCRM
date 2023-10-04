from aiogram import types
from sheet import *
from loader import dp


# Echo bot
@dp.message_handler(text="💲 Daromadim")
async def bot_echo(message: types.Message):
    data1 = await getData2(value_to_find=message.from_user.id, cur=4, table='👥 Xodimlar')
    data = data1[0]
    msg = f"""
ISM, FAMILIYA VA SHARIFINGIZ: <b>{data[1]}</b>

Umumiy daromadingiz: <b>{data[8]}</b>

Umumiy yechib berildi: <b>{data[14]}</b>

Joriy balans: <b>{data[15]}</b>
    """
    await message.answer(text=msg)
