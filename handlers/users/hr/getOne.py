from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.inlineBnt import Penalty, Skip, Confirm
from loader import dp
from sheet import getData1, getAll, addDData
from states.fine import FineState
from typing import Union

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('worker_'))
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    selected = callback_query.data.split('_')[1]
    data = await getData1(selected, 0, "👥 Xodimlar")
    await state.update_data({'id':data[0][0], "name":data[0][1], 'phone':data[0][2], "userId":data[0][20]})
    btn = await Penalty(await getAll("⚙️ Sozlamalar"))
    await callback_query.message.edit_text("⚠️ Jarima sababini tanlang!", reply_markup=btn)
    await FineState.reason.set()


@dp.callback_query_handler(state=FineState.reason)
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    await state.update_data({"reason":callback_query.data})
    data = await getData1(callback_query.data, 129, "⚙️ Sozlamalar")
    print("data",callback_query.data)
    await state.update_data({"price":data[0][130]})
    await callback_query.message.edit_text("<b>✍️ Izoh qoldiring!</b>", reply_markup=Skip())
    await FineState.comment.set()

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'skip', state=FineState.comment)
async def handle_product_deletion(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data({"comment": callback_query.data})
    await edit_fine_message(state, callback_query.message)
    await callback_query.message.delete()

@dp.message_handler(state=FineState.comment)
async def handle_product_deletion(message: types.Message, state: FSMContext):
    await state.update_data({"comment": message.text})
    await edit_fine_message(state, message)


async def edit_fine_message(state: FSMContext, source_message: Union[types.CallbackQuery, types.Message]):
    data = await state.get_data()
    name = data.get("name")
    phone = data.get('phone')
    reason = data.get('reason')
    comment = data.get('comment')
    price = data.get('price')

    if comment == "skip":
        comment = "O`tkazib yuborildi!"

    msg = f"""
    ☑️ <b>Jarima ma’lumotlarini tasdiqlang</b>:
• Xodim: {name}
• Telefon raqam: {phone}
• Jarima sababi: {reason}
• Izoh: {comment}
• Jarima miqdori: {price}
    """

    # Use the correct method based on the source message type
    if isinstance(source_message, types.CallbackQuery):
        await source_message.message.edit_text(msg, reply_markup=Confirm())
    else:
        await source_message.answer(msg, reply_markup=Confirm())

    await FineState.confirm.set()

@dp.callback_query_handler(state=FineState.confirm)
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    await callback_query.message.delete()
    loading_message = await callback_query.message.answer_animation(
        animation='https://t.me/myprojectphotobase90775803200000/67')
    if callback_query.data == "success":
        data = await state.get_data()
        reason = data.get('reason')
        comment = data.get('comment')
        price = data.get('price')
        userID = data.get("userId")

        if comment == "skip":
            comment = "O`tkazib yuborildi!"
        await addDData("d", [[userID, "B"], [reason, "D"], [comment, "E"], [price, "F"]], "🔴 Jarimalar")
        await callback_query.message.answer("<b>☑️ Qabul qilindi!</b>")
    else:
        await callback_query.message.answer(text="<b>❌ Jarima bekor qilindi!</b>")
    await state.finish()
    await loading_message.delete()