from aiogram import types

from keyboards.inline.inlineBnt import createOrdersBtns, btn1, btn2
from secret import ADMIN_ID
from sheet import *
from loader import dp, bot


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('orderId_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    await callback_query.message.delete()
    loading_message = await bot.send_animation(chat_id=callback_query.from_user.id,
                                               animation="https://t.me/myprojectphotobase90775803200000/67",
                                               disable_notification=True)

    test = await find_orders(value_to_find=selected_order_id, cur=0, table='📒 Buyurtmalar', user_id=callback_query.from_user.id)
    if test[0][0][1] == "🔵 yangi buyurtma":
        add = await add_row(rows=[["D", int(test[0][0][0]) + 2, callback_query.from_user.id], ["B", int(test[0][0][0]) + 2, '🟠 konsultatsiya']],table="📒 Buyurtmalar")
        text = await getNotifMsg(add, callback_query.from_user.id, callback_query.from_user.username)
        try:
            await bot.send_message(chat_id=ADMIN_ID, text=text)
        except:
            pass
    if test[0][0][1] == "🟠 konsultatsiya" or test[0][0][1] == "🔵 yangi buyurtma":
        check = test[0][0]
        print(check)
        msg = f"""
Buyurtma tafsilotlari:

<b>👤 Mijoz:</b>
• Ism: <b>{check[7]}</b> 
• Telefon raqam:<b>{check[10]}</b>
• Kartaga ulangan raqam: <b>{check[12]}</b>  

<b>🛒 Buyurtma:</b>
• Mahsulot nomi: <b>{check[22]}</b>
• Nasiya narx: <b>{check[34]}</b> 
• Nasiya muddati: <b>{check[23]}</b> 
• Oylik to'lov: <b>{check[35]}</b> 
• Buyurtma holati: <b>{check[1]}</b> 
• Sana va vaqt: <b>{check[4]}</b>,<b>{check[77]}</b> 

<b>📎 Fayllar:</b>
• Mijozni mahsulot bilan tushgan rasmi: <b>{check[80]}</b> 
• Shartnoma skrinshoti: {'<b>' + check[81] + '</b>' if len(check) > 81 else ''}

<b>🏢 Do'kon:</b>
• Nomlanishi:<b>{check[21]}</b>
• Call-center: <b>{check[20]}</b>
        """
        await bot.send_message(
                chat_id=callback_query.message.chat.id,
                text=msg,
                reply_markup=btn1(selected_order_id)
            )
    else:
        check = test[0][0]
        msg = f"""
Buyurtma tafsilotlari:

<b>👤 Mijoz:</b>
• Ism: <b>{check[7]}</b> 
• Telefon raqam:<b>{check[10]}</b>
• Kartaga ulangan raqam: <b>{check[12]}</b>  

<b>🛒 Buyurtma:</b>
• Mahsulot nomi: <b>{check[22]}</b>
• Nasiya narx: <b>{check[34]}</b> 
• Nasiya muddati: <b>{check[23]}</b> 
• Oylik to'lov: <b>{check[35]}</b> 
• Buyurtma holati: <b>{check[1]}</b> 
• Sana va vaqt: <b>{check[4]}</b>,<b>{check[77]}</b> 

<b>📎 Fayllar:</b>
• Mijozni mahsulot bilan tushgan rasmi: <b>{check[80]}</b> 
• Shartnoma skrinshoti: {'<b>' + check[81] + '</b>' if len(check) > 81 else ''}

<b>🏢 Do'kon:</b>
• Nomlanishi:<b>{check[21]}</b>
• Call-center: <b>{check[20]}</b>
                """
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text=msg,
            reply_markup=btn2(selected_order_id)
        )
    await loading_message.delete()
