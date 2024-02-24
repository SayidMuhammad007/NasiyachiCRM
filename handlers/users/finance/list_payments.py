import datetime

from aiogram import types
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.inlineBnt import Payment
from loader import dp
from sheet import getData1
from states.payment import PaymenState1
import sheet
from keyboards.inline.inlineBnt import paymentDataBtn, Moliya
from loader import dp
from secret import CHANNEL_ID


# Echo bot
@dp.message_handler(text="📋 To'lov hisoblari")
async def bot_echo(message: types.Message):
    data = await sheet.getPaymentData()
    btn = await paymentDataBtn(data)
    await message.answer("Tanlang!", reply_markup=btn)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('paymentData_'))
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    selected = callback_query.data.split('_')[1]
    await state.update_data({'selected_row' : selected})
    data = await getData1(selected, 14, "📋 To'lov hisoblari")
    data = data[0]
    msg = f"""
<b>To’lov:</b>
• Nomlanishi: <b>{data[2]}</b>
• Hisobraqam:  <b>{data[15]}</b>
• To’lov miqdori: <b>{data[10]}</b>
        """
    await state.update_data({'mainId': data[0]})
    await state.update_data({'id': data[14]})
    await state.update_data({'price':data[15]})
    await callback_query.message.answer(text=msg, reply_markup=Payment())
    await callback_query.message.edit_text("Tanlang!!")
    await PaymenState1.change.set()


@dp.callback_query_handler(state=PaymenState1.change)
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    if callback_query.data == 'moliya_0':
        msg = """
        🖼 Iltimos, to’lov <b>skrinshotini</b> yuboring!
        • Ma’lumot formati: <b>JPG</b> yoki <b>JPEG</b>!
            """
        await callback_query.message.edit_text(text=msg)
        await PaymenState1.img.set()
    elif callback_query.data == 'moliya_2':
        await callback_query.message.edit_text("Summani kiriting!")
        await PaymenState1.price.set()
    else:
        data = await sheet.getPaymentData()
        btn = await paymentDataBtn(data)
        await callback_query.message.answer("Tanlang!", reply_markup=btn)
        await state.finish()


@dp.message_handler(state=PaymenState1.price)
async def handle_product_deletion(message: types.Message, state:FSMContext):
    data = await state.get_data()
    selected = data.get('selected_row')
    await state.update_data({'price':message.text})
    data = await getData1(selected, 14, "📋 To'lov hisoblari")
    data = data[0]
    msg = f"""
<b>To’lov:</b>
• Nomlanishi: <b>{data[2]}</b>
• Hisobraqam:  <b>{data[15]}</b>
• To’lov miqdori: <b>{message.text}</b>
    """
    await state.update_data({'id': data[14]})
    await state.update_data({'mainId': data[0]})
    await message.answer(text=msg, reply_markup=Payment())
    await PaymenState1.confirming.set()





@dp.callback_query_handler(lambda callback_query: callback_query.data == 'moliya_0', state=PaymenState1.confirming)
async def bot_echo(callback: types.CallbackQuery):
    msg = """
🖼 Iltimos, to’lov <b>skrinshotini</b> yuboring!
• Ma’lumot formati: <b>JPG</b> yoki <b>JPEG</b>!
    """
    await callback.message.edit_text(text=msg)
    await PaymenState1.img.set()

@dp.message_handler(state=PaymenState1.img, content_types=types.ContentType.PHOTO)
async def get_partner_phone(message: types.Message, state: FSMContext):
    sent_message = await message.copy_to(chat_id="@" + CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({'img':post_link})
    data = await sheet.getDataForDropdown("🆔 Hisobraqamlar!A3:O")
    btn = await Moliya(data)
    await message.answer(text="🆔 Hisobraqamni tanlang!", reply_markup=btn)
    await PaymenState1.id.set()

@dp.message_handler(state=PaymenState1.img, content_types=types.ContentType.ANY)
async def get_partner_phone(message: types.Message, state: FSMContext):
    await message.answer(text="Rasm yuboring!")
@dp.callback_query_handler(state=PaymenState1.id)
async def get_partner_phone(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    loading_message = await callback.message.answer_animation(
        animation='https://t.me/myprojectphotobase90775803200000/67')
    data = await state.get_data()
    partner = data.get("id")
    price = data.get("price")
    img = data.get("img")
    id = callback.data
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H:%M:%S")

    formatted_price = price.replace("\xa0", "").replace(",", ".")
    price_float = float(formatted_price)
    await sheet.addDData("d", [[partner, "B"], [img, "G"], [id, "F"], [price_float, "E"], [date, 'H'], [time, 'I']], "💸 To'lovlar")
    await loading_message.delete()
    await callback.message.answer(f"✅ Qabul qilindi, rahmat!")
    await state.finish()
    data = await sheet.getPaymentData()
    btn = await paymentDataBtn(data)
    await callback.message.answer("Tanlang!", reply_markup=btn)