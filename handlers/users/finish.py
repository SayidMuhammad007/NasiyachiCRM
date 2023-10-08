from aiogram import types
from aiogram.dispatcher import FSMContext
import string
import random
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import mainBtn
from keyboards.default.mainBtn import markets, confirmBtn, menuBtn, times
from keyboards.inline.inlineBnt import *
from secret import ADMIN_ID
from sheet import *
from loader import dp, bot
from states.rasmiylashtirish import Save
CHANNEL_ID = "myprojectphotobase90775803200000"
def random_caption():
    length = 25  # Adjust the length as needed
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('finish_'))
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    selected_order_id = callback_query.data.split('_')[1]
    await state.update_data({'orderId':selected_order_id})
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Shartnoma faolligi scrinshoti!",
            reply_markup=None
        )
    await Save.screen.set()

# @dp.message_handler(state=Save.id)
# async def id(message: types.Message, state:FSMContext):
#     await state.update_data({'id':message.text})
#     await message.answer(text="Bo`lib to`lash muddati", reply_markup=Month())
#     await Save.time.set()
#
# @dp.callback_query_handler(state=Save.time)
# async def id(callback: types.CallbackQuery, state:FSMContext):
#     await state.update_data({'time':callback.data})
#     await callback.message.edit_text(text="Mahsulot nomi")
#     await Save.product.set()
#
# @dp.message_handler(state=Save.product)
# async def id(message: types.Message, state:FSMContext):
#     await state.update_data({'product':message.text})
#     await message.answer(text="Mahsulot narxi")
#     await Save.price.set()
#
#
# @dp.message_handler(state=Save.price)
# async def id(message: types.Message, state:FSMContext):
#     try:
#         price = float(message.text)
#         await state.update_data({'price':message.text})
#         await message.answer(text="Mahsulot rasmi")
#         await Save.image.set()
#     except:
#         await message.answer(text="Faqat son kiriting!")
#         await Save.price.set()
#
#
#
# @dp.message_handler(state=Save.image, content_types=types.ContentType.PHOTO)
# async def id(message: types.Message, state:FSMContext):
#     sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
#     post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
#     print(post_link)
#     await state.update_data({'image':post_link})
#     data = await getAll(table="🏢 Hamkor-do'konlar")
#     btn = await markets(data)
#     await message.answer(text="Hamkor do`konni tanlang!", reply_markup=btn)
#     await Save.market.set()
#
# @dp.message_handler(state=Save.image, content_types=types.ContentType.ANY)
# async def id(message: types.Message, state:FSMContext):
#     await message.answer(text="Rasm yuboring!")
#     await Save.image.set()
#
# @dp.message_handler(state=Save.market)
# async def id(message: types.Message, state:FSMContext):
#     await state.update_data({'market':message.text})
#     await message.answer(text="Mijozning mahsulot bilan rasmi!", reply_markup=ReplyKeyboardRemove())
#     await Save.customer_pic.set()
#
# @dp.message_handler(state=Save.customer_pic, content_types=types.ContentType.PHOTO)
# async def id(message: types.Message, state:FSMContext):
#     sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
#     post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
#     print(post_link)
#     await state.update_data({'customer_pic':post_link})
#     await message.answer(text="Shartnoma faolligi scrinshoti", reply_markup=ReplyKeyboardRemove())
#     await Save.screen.set()

# @dp.message_handler(state=Save.customer_pic, content_types=types.ContentType.ANY)
# async def id(message: types.Message, state:FSMContext):
#     await message.answer(text="Rasm yuboring!")
#     await Save.customer_pic.set()


@dp.message_handler(state=Save.screen, content_types=types.ContentType.PHOTO)
async def id(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    print(post_link)
    await state.update_data({'screen':post_link})
    data = await state.get_data()
    orderId = data.get('orderId')
    # time = data.get('time')
    # product = data.get('product')
    # price = data.get('price')
    # image = data.get('image')
    # market = data.get('market')
    # customer_pic = data.get('customer_pic')
    # screen = data.get('screen')
#     msg = f"""
# Ma`lumotlarni tekshiring
# Mijoz pasport IDsi: {id}
# Bo`lib to`lash muddati: {time}
# Mahsulot nomi: {product}
# Narxi: {price}
# Hamkor do`kon: {market}
# Mahsulot rasmi: {image}
# Mijozni mahsulot bilan rasmi: {customer_pic}
# Shartnoma faolligi skrinshoti: {screen}
#     """
    data0 = await getData2(orderId, 0, "📒 Buyurtmalar")
    a_data = data0[0]
    msg = f"""
👤 Mijoz:
Ism: {a_data[7]}
Telefon raqam: {a_data[11]}
UzumNasiyadan ro'yhatdan o'tgan telefon raqami: {a_data[12]} 

🛒 Buyurtma:
Mahsulot nomi: {a_data[22]}
Mahsulot narxi: {a_data[28]}
Nasiya narx: {a_data[35]}
Oylik to'lov: {a_data[36]}
Buyurtma holati: 🟡 rasmiylashtirilmoqda

📎 Fayllar:
Mijozni mahsulot bilan tushgan rasmi:{'<b>' + a_data[80] + '</b>' if len(a_data) > 80 else ''}
Shartnoma skrinshoti: {'<b>' + a_data[81] + '</b>' if len(a_data) > 81 else ''}
                    """
    await message.answer(text=msg, reply_markup=confirmBtn())
    await Save.confirm.set()

@dp.message_handler(state=Save.screen, content_types=types.ContentType.ANY)
async def id(message: types.Message, state:FSMContext):
    await message.answer(text="Rasm yuboring!")
    await Save.screen.set()


@dp.message_handler(state=Save.confirm)
async def id(message: types.Message, state:FSMContext):
    if message.text == "Tasdiqlash✅":
        data = await state.get_data()
        id = data.get('id')
        # time = data.get('time')
        # product = data.get('product')
        # price = data.get('price')
        # image = data.get('image')
        # market = data.get('market')
        # customer_pic = data.get('customer_pic')
        screen = data.get('screen')
        orderId = data.get("orderId")
        # data0 = await getData2(orderId, 0, "📒 Buyurtmalar")
        # a_data = data0[0]
#         msg = f"""
# 👤 Mijoz:
# Ism: {a_data[7]}
# Telefon raqam: {a_data[11]}
# UzumNasiyadan ro'yhatdan o'tgan telefon raqami: {a_data[12]}
#
# 🛒 Buyurtma:
# Mahsulot nomi: {a_data[22]}
# Mahsulot narxi: {a_data[28]}
# Nasiya narx: {a_data[35]}
# Oylik to'lov: {a_data[36]}
# Buyurtma holati: 🔵 yangi buyurtma
#
# 🏢 Do'kon:
# Nomlanishi:1: SHUKURULLA -> nasiyachi.biz: 950707849
# Call-center: 982767970
#
# 📎 Fayllar:
# Mijozni mahsulot bilan tushgan rasmi:
# Shartnoma skrinshoti: {screen}
#                         """
        data = [
            ["B", int(orderId) + 2, "⚪️ rasmiylashtirildi"],
            ["CD", int(orderId) + 2, screen],
        ]
        await add_row(rows=data)
        notify = await getNotifMsg(int(orderId)+2, message.from_user.id, message.from_user.username)
        await bot.send_message(chat_id=ADMIN_ID, text=notify)
        await message.answer(text="Tasdiqlandi", reply_markup=menuBtn)
        await state.finish()
    else:
        await message.answer(text="❌Bekor qilindi", reply_markup=menuBtn)
        await state.finish()
