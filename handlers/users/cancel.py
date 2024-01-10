from aiogram import types
import json
from keyboards.inline.inlineBnt import *
from secret import ADMIN_ID
from sheet import *
from loader import dp, bot


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancel_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    order_id = await add_row(rows=[["B", int(selected_order_id) + 2, "⛔️ bekor qilindi"]], table="📒 Buyurtmalar")
    text = await getNotifMsg(order_id, callback_query.from_user.id, callback_query.from_user.username)

    try:
        await bot.send_message(chat_id=ADMIN_ID, text=text)

    except:
        pass
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="❌ Bekor qilindi:",
            reply_markup=btn3(selected_order_id)
        )


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancelStatus1_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    order_id = await add_row(rows=[["C", int(selected_order_id) + 2, "Mijoz bilan bog’lanib bo’lmadi"]],table="📒 Buyurtmalar")

    text = await getNotifMsg(order_id, callback_query.from_user.id, callback_query.from_user.username)
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=text)
    except:
        pass
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancelStatus2_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Limit ajratilmadi"]],table="📒 Buyurtmalar")
    text = await getNotifMsg(add, callback_query.from_user.id, callback_query.from_user.username)
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=text)
    except:
        pass
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancelStatus3 _'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Mijoz bekor qildi"]],table="📒 Buyurtmalar")
    text = await getNotifMsg(add, callback_query.from_user.id, callback_query.from_user.username)
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=text)
    except:
        pass
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancelStatus4_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Ma'lumot yetarli emas"]],table="📒 Buyurtmalar")
    text = await getNotifMsg(add, callback_query.from_user.id, callback_query.from_user.username)
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=text)
    except:
        pass
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancelStatus5_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Aloqa o'rnatilmadi"]],table="📒 Buyurtmalar")
    text = await getNotifMsg(add, callback_query.from_user.id, callback_query.from_user.username)
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=text)
    except:
        pass
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancelStatus6_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Mavjud bo'lmagan raqam"]],table="📒 Buyurtmalar")
    text = await getNotifMsg(add, callback_query.from_user.id, callback_query.from_user.username)
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=text)
    except:
        pass
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )