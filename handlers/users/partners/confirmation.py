from aiogram import types

from keyboards.default.mainBtn import markets, cancel
from loader import dp, bot
from sheet import add_row, getAll


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('truePartner_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    await callback_query.message.delete()
    loading_message = await bot.send_animation(chat_id=callback_query.from_user.id,
                                               animation="https://t.me/myprojectphotobase90775803200000/67",
                                               disable_notification=True)
    add = await add_row(rows=[["AU", int(selected) + 3, "📔 O'quv jarayonida!"], ["BA", int(selected) + 3, 1]],table="🏢 Hamkor-do'konlar")
    await callback_query.message.answer(text="✅ Hamkor uchun dostup berildi!")
    await loading_message.delete()


# cancel;

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('falsePartner_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    await callback_query.message.delete()
    loading_message = await bot.send_animation(chat_id=callback_query.from_user.id,
                                               animation="https://t.me/myprojectphotobase90775803200000/67",
                                               disable_notification=True)
    data = await getAll(table="⚙️ Sozlamalar")
    btn = await cancel(data, selected)
    await callback_query.message.answer(text="⚠️ Iltimos, sabablarini tanlang!", reply_markup=btn)
    await loading_message.delete()

