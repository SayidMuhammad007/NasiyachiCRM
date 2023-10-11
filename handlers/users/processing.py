from aiogram import types

from keyboards.inline.inlineBnt import *
from secret import ADMIN_ID
from sheet import *
from loader import dp, bot


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('rasmiy_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    print(callback_query.data)
    add = await add_row(rows=[["B", int(selected_order_id) + 2, "🟡 rasmiylashtirilmoqda"]])
    text = await getNotifMsg(add, callback_query.from_user.id, callback_query.from_user.username)
    await bot.send_message(chat_id=ADMIN_ID, text=text)
    test = await getData(value_to_find=selected_order_id, cur=0, table='📒 Buyurtmalar')
    if test:
        check = test[0]
        msg = f"""
Buyurtma tafsilotlari:

👤 Mijoz:
Ism: <b>{check[7]}</b> 
Telefon raqam:<b>{check[10]}</b>
UzumNasiyadan ro'yhatdan o'tgan telefon raqami: <b>{check[12]}</b>  

🛒 Buyurtma:
Mahsulot nomi: <b>{check[22]}</b>
Mahsulot narxi: <b>{check[28]}</b> 
Nasiya narx: <b>{check[34]}</b> 
Oylik to'lov: <b>{check[35]}</b> 
Buyurtma holati: <b>{check[1]}</b> 
Sana va vaqt: <b>{check[4]}</b>,<b>{check[77]}</b> 

📎 Fayllar:
Mijozni mahsulot bilan tushgan rasmi: <b>{check[80]}</b> 
Shartnoma skrinshoti: {'<b>' + check[81] + '</b>' if len(check) > 81 else ''}

🏢 Do'kon:
Nomlanishi:<b>{check[21]}</b>
Call-center: <b>{check[20]}</b>
        """
        await bot.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=msg,
                reply_markup=btn2(selected_order_id)
            )
