from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.mainBtn import menuBtn, CancelBtn, markets
from keyboards.inline.inlineBnt import RequestBtn, Month, Success, btn2, btn1
from loader import dp, bot
from secret import ADMIN_ID
from sheet import getData, getData1, add_row, getAll, addData, find_orders, getNotifMsg
from states.rasmiylashtirish import Order
import re
CHANNEL_ID = "myprojectphotobase90775803200000"
phone_pattern = r'^\d{9}$|^\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$'
@dp.message_handler(lambda message: message.text in ["/start", "❌ Bekor qilish"], state="*")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Tanlang!", reply_markup=menuBtn)


@dp.message_handler(text='➕ Yangi buyurtma')
async def bot_start(message: types.Message):
    msg = "Mijoz ismi"
    await message.answer(text=msg, reply_markup=CancelBtn())
    await Order.name.set()

@dp.message_handler(state=Order.name)
async def bot_start(message: types.Message, state:FSMContext):
    await state.update_data({"name":message.text})
    await message.answer(text="Telefon raqami(Masalan: 907758032)", reply_markup=CancelBtn())
    await Order.phone.set()


@dp.message_handler(lambda message: not re.match(phone_pattern, message.text), state=Order.phone)
async def invalid_phone_format(message: types.Message):
    await message.answer(
        "Noto`g`ri formatda yozdingiz!(907758032)")


@dp.message_handler(lambda message: re.match(phone_pattern, message.text), state=Order.phone)
async def valid_phone_format(message: types.Message, state: FSMContext):
    await state.update_data({"phone": message.text})
    await message.answer(text="Mahsulot nomi", reply_markup=CancelBtn())
    await Order.product.set()

@dp.message_handler(state=Order.product)
async def bot_start(message: types.Message, state:FSMContext):
    await state.update_data({"product":message.text})
    data = await getAll(table="🏢 Hamkor-do'konlar")
    btn = await markets(data)
    await message.answer(text="Hamkor do`konni tanlang!", reply_markup=btn)
    await Order.market.set()


@dp.message_handler(state=Order.market)
async def bot_start(message: types.Message, state:FSMContext):
    await state.update_data({"market":message.text})
    await message.answer(text="Mahsulot narxi", reply_markup=CancelBtn())
    await Order.price.set()

@dp.message_handler(state=Order.price)
async def bot_start(message: types.Message, state:FSMContext):
    try:
        d = float(message.text)
        await state.update_data({"price": message.text})
        await message.answer("Bo’lib to’lash muddati", reply_markup=Month())
        await Order.time.set()
    except:
        await message.answer(text="Faqat son kiriting!")
        await Order.price.set()


@dp.callback_query_handler(state=Order.time)
async def bot_start(callback: types.CallbackQuery, state:FSMContext):
    await state.update_data({"time":callback.data})
    await callback.message.edit_text(text="UzumNasiyadan ro’yhatdan o’tganmi?", reply_markup=RequestBtn())
    await Order.uzum.set()

@dp.callback_query_handler(state=Order.uzum)
async def bot_start(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == "confirmYes":
        await state.update_data({"uzum":"✅Ha"})
        await callback.message.edit_text(text="UzumNasiyadan ro’yhatdan o’tgan telefon raqamlari(991234567)")
        await Order.uzum_phone.set()
    else:
        await state.update_data({"uzum":"❌Yo`q"})
        await bot.forward_message(chat_id=callback.from_user.id, from_chat_id=-1001978502166, message_id=74)
        await callback.message.answer(text="Tanlang!", reply_markup=Success())
        await Order.check.set()

@dp.callback_query_handler(state=Order.check)
async def bot_start(callback: types.CallbackQuery, state:FSMContext):
    if callback.data == "success":
        await callback.message.edit_text(text="UzumNasiyadan ro’yhatdan o’tgan telefon raqamlari")
        await Order.uzum_phone.set()
    else:
        await callback.message.delete()
        await callback.message.answer(text="Bekor qilindi ❌", reply_markup=menuBtn)
        await state.finish()

@dp.message_handler(state=Order.uzum_phone)
async def bot_start(message: types.Message, state:FSMContext):
    await state.update_data({"uzum_phone": message.text})
    await message.answer(text="Mahsulot bilan tushgan rasmi", reply_markup=ReplyKeyboardRemove())
    await Order.pic.set()

@dp.message_handler(state=Order.pic, content_types=types.ContentType.PHOTO)
async def bot_start(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({"pic":post_link})
    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    price = data.get('price')
    uzum = data.get('uzum')
    uzum_phone = data.get('uzum_phone')
    product = data.get('product')
    market = data.get('market')
    time = data.get('time')
    print(data)
    if time == "6 oy":
#         msg = f"""
# Yuqoridagi ma’lumotlarni tasdiqlang
# Mijoz ismi: {name}
# Telefon raqami: {phone}
# Mahsulot nomi: {product}
# Mahsulot narxi: {price}
# Nasiya narxi: {data[9]}
# Oylik to`lov: {data[12]}
# UzumNasiyadan ro’yhatdan o’tganmi?: {uzum}
# Bo’lib to’lash muddati (6 oy/12 oy): {time}
# UzumNasiyadan ro’yhatdan o’tgan telefon raqamlari: {uzum_phone}
#                     """
        msg = f"""
👤 Mijoz:
Ism: {name}
Telefon raqam: {phone}
UzumNasiyadan ro'yhatdan o'tgan telefon raqami: {uzum_phone} 

🛒 Buyurtma:
Mahsulot nomi: {product}
Mahsulot narxi: {price}
Bo’lib to’lash muddati (6 oy/12 oy): {time}
Buyurtma holati: 🔵 yangi buyurtma

🏢 Do'kon:
Nomlanishi:{market}
                """

    else:
#         msg = f"""
# Yuqoridagi ma’lumotlarni tasdiqlang
# Mijoz ismi: {name}
# Telefon raqami: {phone}
# Mahsulot nomi: {product}
# Mahsulot narxi: {price}
# Nasiya narxi: {data[9]}
# Oylik to`lov: {data[18]}
# UzumNasiyadan ro’yhatdan o’tganmi?: {uzum}
# Bo’lib to’lash muddati (6 oy/12 oy): {time}
# UzumNasiyadan ro’yhatdan o’tgan telefon raqamlari: {uzum_phone}
#                             """
        msg = f"""
👤 Mijoz:
Ism: {name}
Telefon raqam: {phone}
UzumNasiyadan ro'yhatdan o'tgan telefon raqami: {uzum_phone} 

🛒 Buyurtma:
Mahsulot nomi: {product}
Mahsulot narxi: {price}
Bo’lib to’lash muddati (6 oy/12 oy): {time}
Buyurtma holati: 🔵 yangi buyurtma

🏢 Do'kon:
Nomlanishi:{market}
                """

    await state.update_data({'customer_pic':post_link})
    await message.answer(text=msg, reply_markup=RequestBtn())
    await Order.confirm.set()

@dp.message_handler(state=Order.pic, content_types=types.ContentType.ANY)
async def id(message: types.Message, state:FSMContext):
    await message.answer(text="Rasm yuboring!", reply_markup=menuBtn)
    await Order.pic.set()

@dp.callback_query_handler(state=Order.confirm)
async def bot_start(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    await callback.message.delete()
    loading_message = await callback.message.answer_animation(
        animation='https://t.me/myprojectphotobase90775803200000/67')
    if callback.data == "confirmYes":
        data5 = await getData1(value_to_find=callback.from_user.id, cur=4, table="👥 Xodimlar")
        data2 = data5[0]
        print(data2)
        data = await state.get_data()
        name = data.get('name')
        product = data.get('product')
        phone = data.get('phone')
        uzum_phone = data.get('uzum_phone')
        price = data.get('price')
        time = data.get('time')
        pic = data.get('pic')
        market = data.get('market')
        today = datetime.now()

        # Format today's date as a string in the desired format
        formatted_today = today.strftime("%d.%m.%Y")
        formatted_time = today.strftime("%H:%M:%S")
        data = [
            [name, "H"],
            [phone, "K"],
            [product, "W"],
            [price, "AB"],
            ["🔵 yangi buyurtma", "B"],
            [formatted_today, "E"],
            [time, "X"],
            [market, "V"],
            [uzum_phone, "M"],
            [pic, "CC"],
            [formatted_time, "BZ"],
            [callback.from_user.id, "D"],
        ]

        selected_order_id = await addData(data, "📒 Buyurtmalar")

        msg = await callback.message.answer(text="Tasdiqlandi!", reply_markup=menuBtn)
        await loading_message.delete()
        await msg.delete()
        loading_message = await callback.message.answer_animation(
            animation='https://t.me/myprojectphotobase90775803200000/67')
        test = await find_orders(value_to_find=selected_order_id, cur=0, table='📒 Buyurtmalar',
                                 user_id=callback.from_user.id)
        if test[0][0][1] == "🔵 yangi buyurtma":
            add = await add_row(rows=[["D", int(test[0][0][0]) + 2, callback.from_user.id],
                                      ["B", int(test[0][0][0]) + 2, '🟠 konsultatsiya']])
            text = await getNotifMsg(add, callback.from_user.id, callback.from_user.username)
            await bot.send_message(chat_id=ADMIN_ID, text=text)
        check = test[0][0]
        print(check)
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
Bo’lib to’lash muddati:: <b>{check[23]}</b> 
Buyurtma holati: <b>{check[1]}</b> 
Sana va vaqt: <b>{check[4]}</b>,<b>{check[77]}</b> 

📎 Fayllar:
Mijozni mahsulot bilan tushgan rasmi: <b>{check[80]}</b> 
Shartnoma skrinshoti: {'<b>' + check[81] + '</b>' if len(check) > 81 else ''}

🏢 Do'kon:
Nomlanishi:<b>{check[21]}</b>
Call-center: <b>{check[20]}</b>
            """
        await bot.send_message(
            chat_id=callback.message.chat.id,
            text=msg,
            reply_markup=btn1(selected_order_id[1])
        )

        await loading_message.delete()

    else:
        await callback.message.answer(text="Bekor qilindi!", reply_markup=menuBtn)
    await state.finish()