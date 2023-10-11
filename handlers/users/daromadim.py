from aiogram import types
from sheet import *
from loader import dp


# Echo bot
@dp.message_handler(text="💲 Daromadim")
async def bot_echo(message: types.Message):
    data1 = await getData2(value_to_find=message.from_user.id, cur=4, table='👥 Xodimlar')
    data = data1[0]
    msg = f"""
👤 Xodim:
• Ism: <b>{data[1]}</b> 
• Telefon: <b>{data[2]}</b> 
• Lavozim: <b>{data[7]}</b> 

💰 Daromadlar:
— Sotuv: <b>{data[14]}</b> 
— Hamkorlik: <b>{data[21]}</b> 
— Xizmatlar: <b>{data[22]}</b> 

• Umumiy: <b>{data[9]}</b> 
• To'landi: <b>{data[15]}</b> 
• Balans: <b>{data[16]}</b> 
    """
    await message.answer(text=msg)
