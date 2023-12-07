import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.finance.view import current_page, ITEMS_PER_PAGE, generate_message_text
from keyboards.default.mainBtn import menuBtn, PayBtn
from keyboards.inline.inlineBnt import Moliya
from loader import dp
from secret import CHANNEL_ID, ADMIN_ID
from sheet import getDataForDropdown, addData, checkUser, addDData, getAllHaveValueOne
from states.payment import PaymenState


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'moliya_0', state=PaymenState.confirming)
async def bot_echo(callback: types.CallbackQuery):
    msg = """
🖼 Iltimos, to’lov <b>skrinshotini</b> yuboring!
• Ma’lumot formati: <b>JPG</b> yoki <b>JPEG</b>!
    """
    await callback.message.edit_text(text=msg)
    await PaymenState.img.set()

@dp.message_handler(state=PaymenState.img, content_types=types.ContentType.PHOTO)
async def get_partner_phone(message: types.Message, state: FSMContext):
    sent_message = await message.copy_to(chat_id="@" + CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({'img':post_link})
    data = await getDataForDropdown("🆔 Hisobraqamlar!A3:O")
    btn = await Moliya(data)
    await message.answer(text="🆔 Hisobraqamni tanlang!", reply_markup=btn)
    await PaymenState.id.set()

@dp.message_handler(state=PaymenState.img, content_types=types.ContentType.ANY)
async def get_partner_phone(message: types.Message, state: FSMContext):
    await message.answer(text="Rasm yuboring!")
@dp.callback_query_handler(state=PaymenState.id)
async def get_partner_phone(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    loading_message = await callback.message.answer_animation(
        animation='https://t.me/myprojectphotobase90775803200000/67')
    data = await state.get_data()
    partner = data.get("partnerId")
    price = data.get("price")
    img = data.get("img")
    id = callback.data
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H:%M:%S")

    formatted_price = price.replace("\xa0", "").replace(",", ".")
    price_float = float(formatted_price)
    print("id",id,"img", img)
    await addDData("d", [[partner, "B"], [img, "G"], [id, "F"], [price_float, "E"], [date, 'H'], [time, 'I']], "💸 To'lovlar")
    await loading_message.delete()
    await callback.message.answer(f"✅ Qabul qilindi, rahmat!")
    await state.finish()
    from handlers.users.finance.view import data
    data = await getAllHaveValueOne("🏢 Hamkor-do'konlar", "A3:CC", 26, 1)
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE

    text, markup = generate_message_text(start_idx, end_idx)
    await callback.message.answer(text=text, reply_markup=markup)