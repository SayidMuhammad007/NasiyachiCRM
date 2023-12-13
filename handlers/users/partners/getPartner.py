from aiogram import types

from keyboards.default.mainBtn import confirmBtn, confirmBtn0
from loader import dp
from sheet import *


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('PartnerId_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    print("selected", callback_query.data)
    await callback_query.message.delete()
    loading_message = await bot.send_animation(chat_id=callback_query.from_user.id,
                                               animation="https://t.me/myprojectphotobase90775803200000/67",
                                               disable_notification=True)
    print('worker')
    worker = await getData1(value_to_find=callback_query.from_user.id, cur=4, table="👥 Xodimlar")
    partner = await getDataNew(value_to_find=worker[0][19], cur=33, table="🏢 Hamkor-do'konlar")
    print(f"part{partner}")
    if partner and len(partner[0]) > 46 and partner[0][46]:
        selected = partner[0][0]
    else:
        add = await add_row(rows=[["AU", int(selected) + 3, "🟡 Qabul qilindi!"],["BB", int(selected) + 3, callback_query.from_user.username], ["AH", int(selected) + 3, worker[0][19]], ["BA", int(selected) + 3, 0]],table="🏢 Hamkor-do'konlar")
        partner = await getData1(value_to_find=selected, cur=0, table="🏢 Hamkor-do'konlar")
    msg = f"""
<b>👤 Rahbar ma’lumotlari:</b>
Do’kon rahbarining ISM va FAMILIYASI: <b>{partner[0][1]}</b>
Do’kon rahbarining TELEFON RAQAMI: <b>{partner[0][3]}</b>
Do’kon rahbarining E-POCHTASI: <b>{partner[0][4]}</b>

<b>🏢 Do’kon ma’lumotlari:</b>
Do’koningiz nomi: <b>{partner[0][6]}</b>
Do’koningiz telefon raqami: <b>{partner[0][7]}</b>
Do’kon joylashgan manzil: <b>{partner[0][10]}</b>
Do’kon kategoriyasi: <b>{partner[0][40]}</b>
Do'konning instagram sahifasi: <b><a href='{partner[0][47]}'>[LINK]</a></b>
Do'konning telegram sahifasi: <b><a href='{partner[0][48]}'>[LINK]</a></b>
Umumiy filliallar soni: <b>{partner[0][45]}</b>

<b>💰 Moliya ma’lumotlari:</b>
Humo: <b>{partner[0][43]}</b>
Uzcard: <b>{partner[0][44]}</b>

<b>🔗 Fayllar:</b>
Do’kon rahbarining OLD PASPORT RASMI: <b><a href='{partner[0][50]}'>[LINK]</a></b>
Do’kon rahbarining ORQA PASPORT RASMI: <b><a href='{partner[0][51]}'>[LINK]</a></b>
Asosiy do’konning lokatsiyasi: <b><a href='{partner[0][49]}'>[LINK]</a></b>
Dokonning ichki rasmi: <b><a href='{partner[0][41]}'>[LINK]</a></b>
Do’konning tashqi rasmi: <b><a href='{partner[0][42]}'>[LINK]</a></b>

<b>Ma’lumotlar to’g’riligini tekshiring va tasdiqlang!</b> 
"""
    print(f"idd{selected}")
    await callback_query.message.answer(text=msg, reply_markup=confirmBtn0(selected))
    await loading_message.delete()
