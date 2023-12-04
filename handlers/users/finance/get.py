from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.inlineBnt import Payment
from loader import dp
from sheet import getData1
from states.payment import PaymenState


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('partnerMoney_'))
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    selected = callback_query.data.split('_')[1]
    data = await getData1(selected, 0, "🏢 Hamkor-do'konlar")
    data = data[0]
    msg = f"""
<b>Subyekt ma’lumotlari:</b>
• Qabul qiluvchi: <b>{data[1]}</b>
• Telefon raqam:  <b>{data[3]}</b>
• Do’kon nomi:  <b>{data[6]}</b>

<b>To’lov ma’lumotlari:</b>
• {data[43] if len(data) > 43 else ''}: <b>{data[44] if len(data) > 44 else ''}</b>
• To’lov miqdori: <b>{data[25]}</b>
    """
    await state.update_data({'partnerId': data[28]})
    await state.update_data({'partnerMainId': data[0]})
    await state.update_data({'price': data[25]})
    print("Asdf")
    await callback_query.message.edit_text(text=msg, reply_markup=Payment())
    await PaymenState.confirming.set()

