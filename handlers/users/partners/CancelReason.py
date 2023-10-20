from aiogram import types

from loader import dp, bot
from sheet import add_row


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('cancelReason_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[2]
    print(selected)
    await callback_query.message.delete()
    loading_message = await bot.send_animation(chat_id=callback_query.from_user.id,
                                               animation="https://t.me/myprojectphotobase90775803200000/67",
                                               disable_notification=True)
    add = await add_row(rows=[["AU", int(selected) + 3, "❌ Bekor qilish"]], table="🏢 Hamkor-do'konlar")
    await callback_query.message.answer(text="❌ Bekor qilindi")
    await loading_message.delete()