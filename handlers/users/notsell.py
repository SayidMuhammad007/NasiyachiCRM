from aiogram import types
import json
from keyboards.inline.inlineBnt import *
from sheet import *
from loader import dp, bot


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('notsell_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["B", int(selected_order_id) + 2, "🔴 sotilmadi"]])
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="⛔️SOTILMADI",
            reply_markup=btn4(selected_order_id)
        )


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('notsellStatus1_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Narx qimmatlik qildi"]])
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('notsellStatus2_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Yaroqsiz mahsulot"]])
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('notsellStatus3_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected_order_id = callback_query.data.split('_')[1]
    add = await add_row(rows=[["C", int(selected_order_id) + 2, "Shartlarga to’g’ri kelmadi"]])
    await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Muvaffaqiyatli bekor qilindi"
        )
